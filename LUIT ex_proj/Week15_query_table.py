import boto3
from boto3.dynamodb.conditions import Key

client = boto3.resource('dynamodb', region_name='us-east-1')
table = client.Table('Birthdays')

response = table.query(KeyConditionExpression=Key('Year').eq('2016') and ('Name').eq('Kiyah Gibson'))


print("The query returned the follow people born in 2016:")
for item in response['Items']:
    print(item)