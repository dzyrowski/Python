import boto3
from boto3.dynamodb.conditions import Key

client = boto3.client('dynamodb', region_name='us-east-1')

response = client.query(
    TableName='Birthdays',
    ExpressionAttributeValues={
        ':ident':{
            'S': 'Amy Gibson',
        },
    },
    KeyConditionExpression='Person = :ident',
    ProjectionExpression='Birthyear'
)

print(response['Items'])