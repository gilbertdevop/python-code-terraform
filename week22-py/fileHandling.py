with open("python.txt", 'w') as f:    # 'w', 'r', 'a'
    f.write("this is the first line \n")
    f.write("this is the second line \n")
    f.write("Devops\n")
    f.write("Success\n")

with open("python.txt", 'r') as f1:   
    m=f1.readline()
    print(m)


#f=open("python.txt", 'w')
#
#f.close