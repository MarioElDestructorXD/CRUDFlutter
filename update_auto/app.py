import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Vehiculos')


def lambda_handler(event, context):
    data = json.loads(event['body'])
    item_id = event['pathParameters']['id']

    response = table.update_item(
        Key={'id': item_id},
        UpdateExpression="set marca=:m, modelo=:mo, potencia=:p, tipo=:t",
        ExpressionAttributeValues={
            ':m': data['marca'],
            ':mo': data['modelo'],
            ':p': data['potencia'],
            ':t': data['tipo']
        },
        ReturnValues="UPDATED_NEW"
    )

    return {
        'statusCode': 200,
        'body': json.dumps(response['Attributes'])
    }
