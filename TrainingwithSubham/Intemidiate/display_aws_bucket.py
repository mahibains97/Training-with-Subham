import boto3
import awsclidriver
s3 = boto3.resource("s3")

def show_buckets(s3_resource):
    for bucket in s3_resource.buckets.all():
        print(bucket.name)
show_buckets(s3)

