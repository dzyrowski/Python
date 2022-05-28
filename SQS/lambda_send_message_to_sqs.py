import json
import boto3
from datetime import datetime


def lambda_handler(event, context):
 
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    sqs = boto3.client('sqs')
    sqs.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/509846243812/Week15project",
        MessageBody=date_time
    )