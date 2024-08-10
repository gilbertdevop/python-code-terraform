#import awscode
from awscode import listInstances, stopInstance

dev_filter= {'Name': 'tag:env', 'Values': ['dev']}

stop= listInstances(dev_filter)
stopInstance(stop)

