

import os
import platform
import psutil

#print(platform.system())
if 'Windows' in platform.platform():
    print("this is a windows system")
    cpu_count= os.cpu_count()
    mem_info= psutil.virtual_memory().total
    os_version= platform.system()
    python_version = platform.python_version()

    print(f"""
          number of cpu: {cpu_count} 
          total memory: {mem_info/(1024**3):.2f} GB 
          os version: {os_version} 
          python version: {python_version}""")
    

else:
    #print("this is a Linux System")  
    pass
