#how to delete VPC

import boto3

client=boto3.client("ec2")
client.delete_vpc(VpcId="vpc-0cf07e5548c968c48")
