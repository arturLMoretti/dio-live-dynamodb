import os
import boto3


class DynamoDB:
    def __init__(self):
        self.dynamodb = boto3.resource(
            "dynamodb",
            region_name=os.environ.get("AWS_REGION"),
            aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
        )

    def create_item(self, table_name, item):
        response = self.dynamodb.Table(table_name).put_item(Item=item)

        if "Attributes" in response:
            item = response["Attributes"]
            return item
        else:
            return None

    def get_item(
        self,
        table_name,
        primary_key,
        primary_key_value,
        secondary_key,
        secondary_key_value,
    ):
        response = self.dynamodb.Table(table_name).get_item(
            Key={primary_key: primary_key_value, secondary_key: secondary_key_value},
        )

        if "Item" in response:
            item = response["Item"]
            return item
        else:
            return None

    def update_item(
        self,
        table_name,
        primary_key,
        primary_key_value,
        secondary_key,
        secondary_key_value,
        update_expression,
        expression_attribute_values,
    ):
        response = self.dynamodb.Table(table_name).update_item(
            Key={primary_key: primary_key_value, secondary_key: secondary_key_value},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
        )

        if "Attributes" in response:
            item = response["Attributes"]
            return item
        else:
            return None

    def delete_item(
        self, table, primary_key, primary_key_value, secondary_key, secondary_key_value
    ):
        response = table.delete_item(
            Key={primary_key: primary_key_value, secondary_key: secondary_key_value},
        )

        if "Attributes" in response:
            item = response["Attributes"]
            return item
        else:
            return None

    def query(
        self,
        table_name,
        index_name,
        key_condition_expression,
        expression_attribute_values,
    ):
        response = self.dynamodb.Table(table_name).query(
            IndexName=index_name,
            KeyConditionExpression=key_condition_expression,
            ExpressionAttributeValues=expression_attribute_values,
        )

        if "Items" in response:
            items = response["Items"]
            return items
        else:
            return None
