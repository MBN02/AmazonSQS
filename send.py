import sys
import boto3

sqs=boto3.client('sqs')
queue_url=''
response=sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=(sys.argv[1])
    )

print(response['MessageId'])
