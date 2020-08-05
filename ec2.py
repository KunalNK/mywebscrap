import boto3
ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-09d8b5222f2b93bf0',
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='myec2web'
 )