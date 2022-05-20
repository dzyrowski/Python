#how to describe VPC using python

import boto3

client=boto3.client("ec2")

#how to describe number of available vpc in your account
print(client.describe_vpcs())

#print number of vpcs in your account
x=client.describe_vpcs()
no_of_vpcs=x["Vpcs"]
print(len(no_of_vpcs))

#how to print the VPC ids, 
for vpc in no_of_vpcs:
    print(vpc["VpcId"]) #VpcId is a part of the dictionary printed when you describe the vpc.
                        # you can change it to any of the descriptions in the dictionary

for vpc in no_of_vpcs:
    print(vpc["CidrBlock"])
    
#how to describe one vpc based on vpc id
print(client.describe_vpcs(VpcIds=["vpc-0a830767acc75197b"]))

