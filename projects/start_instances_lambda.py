import boto3

ec2= boto3.client('ec2', region_name="us-east-1")
# _iam= boto3.client('iam', region_name= 'us-east-1')
# _s3= boto3.client('s3')

dev_filter= {'Name': 'tag:env', 'Values': ['dev']}
qa_filter= {'Name': 'tag:env', 'Values': ['qa']}
prod_filter= {'Name': 'tag:env', 'Values': ['prod']}
stopped_instance= { 'Name': 'instance-state-name','Values': ['stopped']}
Instance_type_filter= [{'Name': 'instance-type', 'Values': ['t2.xlarge'] }]

def listInstances(dev_filter):   # kwargs
     try:
        response= ec2.describe_instances(Filters=[dev_filter])
        #print(response)
        instance_list= []
        for instance in response['Reservations']:
            #print(instance['Instances'][0]['InstanceId'])
            #print("************************************************************")
            instance_id= instance['Instances'][0]['InstanceId']
            instance_list.append(instance_id)
      
        return instance_list
     except Exception as e:
         print(f"Error: {e}")


def startInstance(instance_list):
    try:  
       ec2.start_instances(InstanceIds=instance_list)
    except Exception as e:
        print(f"Error: {e}")


def stopInstance(instance_list):
    try:  
       ec2.stop_instances(InstanceIds=instance_list)
    except Exception as e:
        print(f"Error: {e}")

def main():
    s=listInstances()
    startInstance(s)

    if __name__ == "__main__":
      main()          