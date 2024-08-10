"""
    write a script that will ask for a sting and tell 
    if a letter in the string is a vowel or consonant
"""

my_string= input("please enter your word: ").strip() #string() is used to avoid space
num_c=0
num_v=0

for i in my_string:
    if i in 'aeiou':
        #print(f"{i} is a vowel")
        num_v=num_v+1
    else:
        #print(f"{i} is a consonant")    
        num_c=num_c+1

print(f"number of vowel is: {num_v}")
print(f"umber of consonant is : {num_c}")

