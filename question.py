"""
write a script that will ask user for to enter yes or no as answer
If the user anser is not either yes or no the script should keep asking for a valid entry.
and if the entry is yes or no, then it should display valid entry
"""

x=""
while True:
    if x not in ['yes', 'no']:
       x=input("Do you want covid shot? enter yer or no: ").strip().lower()
    else:
        print("valid choice")
        break
    
