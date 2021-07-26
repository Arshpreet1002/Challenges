import boto3
import sys
import json 
import datetime
from json import JSONEncoder

#defining function to get details of EC2
def getEC2Instances(instance_id):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(InstanceIds=[instance_id])
    return response
class DateTimeEncoder(JSONEncoder):
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

# Enter the Instance ID
instance_id=input("Enter the Instance ID:")  

#Calling the function
response = getEC2Instances(instance_id)         
with open("data_file.json", "w") as write_file:
    json.dump(response, write_file,cls=DateTimeEncoder)

#Getting particular data Key
for instance in response['Reservations']:
    state = instance['Instances'][0]['State']['Name']
    privateIPs = instance['Instances'][0]['PrivateIpAddress']
    print(state)
    print(privateIPs)
