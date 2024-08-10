
z=input("enter your zip code:  ")
print(len(z))
l=len(z)

if (l==5 and z.isdigit()):
    print("good zipcode")
else:
    print("bad zipcode try again")    
