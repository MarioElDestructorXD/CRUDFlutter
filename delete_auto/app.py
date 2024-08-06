import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Vehiculos')


def lambda_handler(event, context):
    item_id = event['pathParameters']['id']

    response = table.delete_item(
        Key={'id': item_id}
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'deleted': True})
    }
