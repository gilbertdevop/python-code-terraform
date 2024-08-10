
email=input("enter your email address please: ")
# l=len(my_string)

if ('@' not in email and email.count('@')==1):
    print("good email")
else:
    print("invalid email try again")    


    """check the different value given by the user.
apply this rule (truth table)

- with and
True and True = True
True and False = False
False and True = False
False and False = False
 
- with or
True or True = True
True or False = True
False or True = True
False or False = False
"""