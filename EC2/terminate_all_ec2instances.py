import boto3

ec2=boto3.client("ec2")

x = ec2.describe_instances()

data = x['Reservations']

li=[]
for instances in data:
    instance = instances['Instances']
    for ids in instance:
        instance_id=ids["InstanceId"]
        li.append(instance_id)
        
ec2.terminate_instances(InstanceIds=li)
