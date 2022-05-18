import boto3

s3=boto3.client('s3')

#delete single object
s3.delete_object(Bucket='bucketname5162022', Key='15-4.PNG')

#find all objects in bucket
objects = s3.list_objects(Bucket='bucketname5162022')["Contents"]

#delete multiple objects

for object in objects:
   s3.delete_object(Bucket='bucketname5162022', Key=object["Key"])
