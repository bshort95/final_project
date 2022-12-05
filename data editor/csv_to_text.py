import csv

with open('.//pre csv//text1.csv', encoding="UTF-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    counter = 1
    for row in csv_reader:
        fc = open(".\\raw data" + "\\job_from_excell2" + str(counter) + ".txt","w",encoding="UTF-8")
        fc.write(row[2])
        fc.close()
        counter = counter + 1        
   