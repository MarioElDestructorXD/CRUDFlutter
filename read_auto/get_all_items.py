import json
from common.db import get_dynamodb_table

def lambda_handler(event, context):
    table = get_dynamodb_table()

    response = table.scan()
    items = response.get('Items', [])

    return {
        'statusCode': 200,
        'body': json.dumps(items)
    }
