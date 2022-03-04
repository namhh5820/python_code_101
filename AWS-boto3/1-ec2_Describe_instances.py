import boto3
import json

ec2 = boto3.client('ec2')
response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'tag:MONITOR',
            'Values': [
                'OFF',
            ]
        },
    ]
)


#LIST VM WITH TAG
for i in response.items():
    print('List VM with tag:MONITOR = OFF: \n', i)

#LIST VM WITH TAG NAME
response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [
                'namhh-1',
            ]
        },
    ]
)

for i in response.items():
    print('\n\n\nList VM with tag:Name = namhh-1: \n', i)