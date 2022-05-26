import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.create_table(
    TableName='Birthdays',
    KeySchema=[
        {
            'AttributeName': 'Person',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'Birthyear',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Person',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Birthyear',
            'AttributeType': 'N'
        },
    ],
     ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)
print("Table status:", table.table_status)

