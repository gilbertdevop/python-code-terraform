#code that will take a string from user , and display how many characters are in that string

my_string=input("enter your name: ")
l=len(my_string)

print(f"your name has {l} character long ")

# print(len(input("enter your name")))

if l<4:
   print( "sorry your name is too short")
else:
   print("good name")

    

