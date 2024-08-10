x=input("enter num1: ")
y=input("enter num2: ")

a=x.strip() #this remove space before and after the enter word
b=y.strip()

if a.replace('-',"").isdigit() and b.replace('-',"").isdigit():

     add = int (a) + int (b)
     print(f"the sum is: {add}")
else:
    print("bad number")     


