import json
from common.db import get_dynamodb_table

def lambda_handler(event, context):
    table = get_dynamodb_table()
    item_id = event['pathParameters']['id']

    table.delete_item(Key={'id': item_id})

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Item deleted'})
    }
