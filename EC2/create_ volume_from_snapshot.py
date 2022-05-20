import boto3
ec2_client=boto3.client('ec2')

ec2_client.create_volume( 
    AvailabilityZone= 'us-east-1d',
    Encrypted=True,
    Size=12,
    SnapshotId='snap-033642c4ddef45db6',
    VolumeType='gp2')