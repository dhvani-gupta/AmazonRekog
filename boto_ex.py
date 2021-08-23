import boto3
from pprint import pprint

s3 = boto3.resource('s3')

print(s3.buckets.all())

for bucket in s3.buckets.all():
    print(bucket)

print("hi")
ec2 = boto3.resource('ec2')
print("\n EC2 instances")
for ins in ec2.instances.all():
    print(ins.id, ins.state)
