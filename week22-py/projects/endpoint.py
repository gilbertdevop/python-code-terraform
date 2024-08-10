import requests

# response= requests.get("http://google.com")

# #s_code= response.status_code 
# #print(s_code)

# if response.status_code==200:
#     isUp= True

# else:
#    isUp= False

# print(isUp)   

#--------------------------------------------------------------------
# We have 5 applications that we support and need a way to petiodically check each endpoint if it is up
#provide a solution for this.

urls= ['http://google.com', 'http://netflix.com', 'http://wikipedia.com', 'http://amazom.com']

for  link in urls:
    resp = requests.get(link)
    if resp.status_code == 200:
        print(f"{link} is up")
    else:
        print(f"{link} is down")
