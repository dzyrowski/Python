import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.create_table(
    TableName='Birthdays',
    KeySchema=[
        {
            'AttributeName': 'Name',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'Year',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Name',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Year',
            'AttributeType': 'N'
        },
{
            'AttributeName': 'Month',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Ye
            'AttributeType': 'N'
        },
    ],
     ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)