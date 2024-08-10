import boto3

_ec2= boto3.client('ec2', region_name='us-east-1')

response= _ec2.describe_instances()

isinstance_list=[]
for item in response['Reservations']:
    #print("***********************************************************************")
    #print(item['Instances'][0]['InstancesId'])
    isinstance_list.append(item['Instances'][0]['InstancesId'])
    print(isinstance_list)

try:    
   _ec2.start_instances(InstanceIds=isinstance_list)
except Exception as e:
   print(f"Error :{e}")

