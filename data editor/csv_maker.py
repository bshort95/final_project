import csv
from walker import walker

walker(".\\pre csv data", "data.txt")
header = ['text', 'mask']
strings = []
datadata = []
def cutter(lis):
    bob = lis.split(" ")    
    temp_list= []

    fs = True
    s = 0
    e = 200
    inc = 200
    while fs:
        if e > len(bob)-1:
            e = len(bob)-1
            fs = False
        
        temp_list.append(" ".join(bob[s:e]))
        s=s + inc 
        e=e + inc

    return temp_list


for f in open("data.txt","r", encoding="UTF-8"):
    try:
        for j in open(f.strip(),"r", encoding="UTF-8"):
            strings.append(j)
    except:
        print(f)



for s in strings:
    temp = s.split("|")
    t1 = cutter(temp[0])
    t2 = cutter(temp[1])
    for i in range(len(t1)):
        datadata.append([t1[i],t2[i]])
    

with open('.\\csv data\\data.csv', 'w', encoding='UTF-8',newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    for d in datadata:
        writer.writerow(d)