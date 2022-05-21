import boto3

client = boto3.client('dynamodb', region_name='us-east-1')

response = client.delete_item(
    TableName='Birthdays',
    Key={'Year': {'N': '1970'}, 'Name': {'S': 'Dennis Zyrowski'},
    }
)

    