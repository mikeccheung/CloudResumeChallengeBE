import boto3
import json

dynamodb = boto3.client('dynamodb')
def handler(event, context):
    response = dynamodb.update_item(
        TableName='resume-HelloHitCounterHits7AAEBF80-1B4E9KHVP4063',
        Key={
            'path': {
                'S': '/visit'
            }
        },
        UpdateExpression='SET hits = hits + :inc',
        ExpressionAttributeValues={
            ':inc': {'N': '1'}
        },
        ReturnValues="UPDATED_NEW"
    )
    res = dynamodb.get_item(
        TableName='resume-HelloHitCounterHits7AAEBF80-1B4E9KHVP4063',
        Key={
            'path': {
                'S': '/visit'
            }
        },
    )
    
    return { 
        'statusCode': 200,
        'body': json.dumps({'count' : response['Attributes']['hits']['N']}),
        'headers' : {
         'Access-Control-Allow-Origin': '*',
         'Access-Control-Allow-Credentials': 'true',
        }
    }