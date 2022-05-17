import boto3

s3_resource=boto3.client('s3')
#s3_resource.list_buckets()

for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket["Name"])
    print(bucket["CreationDate"])
    
    






