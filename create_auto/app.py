import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Vehiculos')


def lambda_handler(event, context):
    data = json.loads(event['body'])

    item = {
        'id': str(uuid.uuid4()),
        'marca': data['marca'],
        'modelo': data['modelo'],
        'potencia': data['potencia'],
        'tipo': data['tipo']
    }

    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
