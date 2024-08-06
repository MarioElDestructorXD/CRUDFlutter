import json
from common.db import get_dynamodb_table


def lambda_handler(event, context):
    table = get_dynamodb_table()
    item = json.loads(event['body'])

    table.put_item(Item=item)

    return {
        'statusCode': 201,
        'body': json.dumps(item)
    }
