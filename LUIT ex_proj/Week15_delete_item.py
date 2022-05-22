import boto3

client = boto3.client('dynamodb', region_name='us-east-1')

response = client.delete_item(
    TableName='Birthdays',
    Key={'Person': {'S': 'Dennis Zyrowski'}, 'Year': {'N': '1970'}, 
    }
)

    