import boto3

def lambda_handler(event, context):
    if not bool(event):
        raise Exception('No event defined!')
        
    instances = event.get("instances")
    region = event.get("region")
        
    if not bool(instances):
        raise Exception('Instances are not defined!')
        
    if not type(instances) is list:
        raise Exception('Instances is not a list!')
        
    if not bool(instances):
        raise Exception('No instances defined')

    if not bool(region):
        raise Exception('Region is not defined!')
        
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.start_instances(InstanceIds=instances)
    
    for instance in instances:
         print("Started {} instance in {} region".format(instance, region))