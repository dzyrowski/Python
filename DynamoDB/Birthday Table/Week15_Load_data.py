import boto3
import json

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Birthdays')

with open("Birthday_data.json") as json_file:
    Birthdays = json.load(json_file)
    for Birthday in Birthdays:
        Person = Birthday['Person'] 
        Birthyear = int(Birthday['Birthyear'])
        info = Birthday['info']

        print("Adding person:", Person, Birthyear)

        table.put_item(
           Item={
               'Person': Person,
               'Birthyear': Birthyear,
               'info': info,
            }
        )
