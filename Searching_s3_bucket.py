import boto3

resource=boto3.resource("s3")
print(list(resource.buckets.all()))  #prints bucket name
print(len(list(resource.buckets.all())))   #prints number of buckets 

#ran as a function
#for bucket in resource.buckets.all():  
    
    #print(bucket.name)  #list bucket name
    
    
    
    
    
    