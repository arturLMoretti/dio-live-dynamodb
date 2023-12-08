from src.services.dynamo import DynamoDB

# Especificando a tabela
table_name = "Music"

# Query por chave primária e secundária
primary_key = "Artist"
primary_key_value = "Iron Maiden"

secondary_key = "SongTitle"
secondary_key_value = "Chains of Misery"

# Obtendo o item da tabela
response = DynamoDB().get_item(
    table_name=table_name,
    primary_key=primary_key,
    primary_key_value=primary_key_value,
    secondary_key=secondary_key,
    secondary_key_value=secondary_key_value,
)

print(response)


# Query por index
index_name = "AlbumTitle-index"

response1 = DynamoDB().query(
    table_name,
    index_name,
    "AlbumTitle = :album_title",
    {":album_title": "Fear of the Dark"},
)

print(response1)
