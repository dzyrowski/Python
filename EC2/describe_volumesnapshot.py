import boto3
ec2_client=boto3.client('ec2')

print(ec2_client.describe_snapshots(
    SnapshotIds=['snap-0ff840a77da1525a6']))
    
    