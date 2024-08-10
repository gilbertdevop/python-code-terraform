import os

#define the function
def hello():
    print("hello serge")

#how to call the function
#hello() 

def hello1(name):
    print(f"hello {name}")

hello1("Romeo")   

def add(x,y):
    print(x+y)

#s=add(5,3)
#print(s)

def commands(cmd):
    os.system(cmd)
#commands('cmd')

def ClearScreen():
    os.system('clear')

