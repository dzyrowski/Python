import boto3

s3=boto3.client('s3')

objects=s3.list_objects(Bucket="bucketname5162022")

for obj in objects['Contents']:
    print(obj['Key'])




