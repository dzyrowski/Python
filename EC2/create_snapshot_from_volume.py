import boto3
ec2_client=boto3.client('ec2')

ec2_client.create_snapshot( 
    Description='snapshot from basevolume using python', 
        VolumeId='vol-00850297c98e16591')
    
