#creating a bucket with an s3 bucket with boto3 python

import boto3

aws_resource=boto3.resource("s3")  #naming the resource we will be creating...in this case s3
bucket=aws_resource.Bucket("bucketname5162022")  #naming the bucket

response = bucket.create(
    ACL='public-read',  #setting access to bucket, you can also set it to ACL='private'|'public-read'|'public-read-write'|'authenticated-read',
  )
    
print(response)
