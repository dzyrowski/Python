import boto3

sqs = boto3.resource('sqs')

queue = sqs.create_queue(QueueName = 'Week15project')

print(queue.url)
