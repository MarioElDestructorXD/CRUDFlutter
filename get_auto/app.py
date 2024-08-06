import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Vehiculos')

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Type {obj.__class__.__name__} not serializable")

def lambda_handler(event, context):
    try:
        response = table.scan()
        items = response.get('Items', [])
        return {
            'statusCode': 200,
            'body': json.dumps(items, default=decimal_default)  # Usa el codificador personalizado
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
