import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('YourTableName')
    item_id = event['pathParameters']['id']

    response = table.delete_item(Key={'id': item_id})

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Item deleted'})
    }
