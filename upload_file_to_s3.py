import boto3

#how to upload a single file
s3=boto3.client("s3")
s3.upload_file('15-4.PNG', 'bucketname5162022', '15-4.PNG')

    

