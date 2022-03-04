#  python3 hello.py
#  apt install python3-pip
#  pip3 list
#  pip3 install boto3
#  aws configure

import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
print('-----------------List my buckets-----------------')
for bucket in s3.buckets.all():
    print(bucket.name)


# Upload a new file
data = open('/root/k8s/kuard-rs.yaml', 'rb')
s3.Bucket('namhh-demo').put_object(Key='kuard-rs.yaml', Body=data)


# List file in my bucket
my_bucket = s3.Bucket('namhh-demo')
print('-----------------List files-----------------')
for file in my_bucket.objects.all():
    print(file.key)
