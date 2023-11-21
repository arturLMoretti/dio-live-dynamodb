import boto3
import os

# Configurando o cliente DynamoDB
region_name = os.environ.get('AWS_REGION')
aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
dynamodb = boto3.resource(
    'dynamodb',
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
    )

# Especificando a tabela
table_name = 'Music'
table = dynamodb.Table(table_name)

# Query por chave primária e secundária
primary_key = 'Artist'
primary_key_value = 'Iron Maiden'

secondary_key = 'SongTitle'
secondary_key_value = 'Chains of Misery'

# Obtendo o item da tabela
response = table.get_item(
    Key={
        primary_key: primary_key_value,
        secondary_key: secondary_key_value
    },
)

# Verificando se o item foi encontrado
if 'Item' in response:
    item = response['Item']
    print(f'Item encontrado: {item}')
else:
    print('Item não encontrado.')


# Query por index
index_name = 'AlbumTitle-index'

response1 = table.query(
    IndexName=index_name,
    KeyConditionExpression='AlbumTitle = :album_title',
    ExpressionAttributeValues={
        ':album_title': 'Fear of the Dark'
    }
)

# Verificando se o item foi encontrado
if 'Items' in response1:
    item = response1['Items']
    print(f'Item encontrado: {item}')
else:
    print('Item não encontrado.')
