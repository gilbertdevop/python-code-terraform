from awscode  import listInstances, startInstance

dev_filter= {'Name': 'tag:env', 'Values': ['dev']}


start= listInstances(dev_filter)
startInstance(start)