
import csv

with open("test.csv" , 'w', newline='') as f:
    write= csv.writer(f)
    HEADER=['Name', 'cell', 'profession', 'email']
    write.writerow(HEADER)
    write.writerow(['serge', '5555 5555 5555555', 'devops engineer', 'gilbert@mannn.com'])
