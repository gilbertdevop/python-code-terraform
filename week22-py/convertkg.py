kg_value = input("Give your kgs value ?  ")


 # as we know  1kg = 2.20462 pound

CONST = 2.20462

kg_value = kg_value.strip() # remove any space

a1 = kg_value.replace(".","").replace(",","").replace("-","")  #remove dot, comma, and negative sign in front of the entry number 


if a1.isdigit():
   pounds = float(kg_value) * CONST 

   print(f"your value is : {kg_value}kgs = {pounds:.3f} pounds")    #format the result to 3 decimal number using ".3f"

else: 
    print("Please enter a numeric value !!!!")
