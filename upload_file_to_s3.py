import boto3

#how to upload a single file
s3=boto3.client("s3")

s3.meta.client.upload_file(Filename = 'C:/Users/dlgibson/Desktop/LUIT/apache.txt', Bucket = 'bucketname5162022', Key = 'apache.txt')

    

