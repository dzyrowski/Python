import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Birthdays')

with open("Birthday_data.json") as json_file:
    Birthdays = json.load(json_file)
    for Birthday in Birthdays:
        Name = Birthday['Name'] 
        Year = int(Birthday['Year'])
        info = Birthday['info']

        print("Adding person:", Name, Year)

        table.put_item(
           Item={
               'Name': Name,
               'Year': Year,
               'info': info,
            }
        )
