import json
from common.db import get_dynamodb_table

def lambda_handler(event, context):
    table = get_dynamodb_table()
    item_id = event['pathParameters']['id']

    response = table.get_item(Key={'id': item_id})
    item = response.get('Item')

    if item:
        return {
            'statusCode': 200,
            'body': json.dumps(item)
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'Item not found'})
        }

