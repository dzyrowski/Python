import boto3

def lambda_handler(event, context):
  
#list all regions
    account_id = boto3.cline('sts').get_caller_identity().get('Account')
    ec2 = boto3.client('ec2')
    regions = [region['RegionName']
        for region in ec2.describe_regions()['Regions']]
        
#list instances in each region
    for region in regions:
        print('Region:', region)
        ec2 = boto3.client('ec2', region_name=region)
        
        response = ec2.describe_snapshots(OwnerIds=[account_id])
        snapshots = response["Snapshots"]
        
        #Sort snapshots by date ascending
        snapshots.sort(key=lambda x: x["StartTime"])
        
        #Remove snapshots we want to keep (ie 3 most recent)
        snapshots = snapshots[:-3]
        
        for snapshot in snapshots:
            id = snapshot['SnapshotId']
            try:
                print("Deleting snapshot:", id)
                ec2.delete_snapshot(SnapshotId=id)
            except Exception as e:
                if 'InvalidSnapshot.InUse' in e.message:
                    print("Snapshot {} is use, skipping.".format(id))
                    continue
            
            
            
            
            
            
            