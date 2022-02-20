import time
import boto3
import mysql.connector

queue_url=''

host = '' 
user = ''
password = ''
database=''

sqs=boto3.client('sqs')

mydb = mysql.connector.connect(host=host, user=user, password=password, database=database) 
mycursor = mydb.cursor()

response = sqs.receive_message(
    QueueUrl=queue_url) 
    
message = response['Messages'][0]

receipt_handle=message['ReceiptHandle']
sqs.delete_message( 
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
    )
    
print('Received and deleted message: %s' % message["Body"])

customerDetails = message["Body"]
customerDetailsList = customerDetails.split(',')
name = customerDetailsList[0]
address = customerDetailsList[1]
val = (name, address)

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
mycursor.execute(sql, val) 
mydb.commit()
print("Record inserted in the DB")
