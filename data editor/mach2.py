from walker import walker
import re
queue_filename = "queue.txt"
file_names = []
str_list = []

labels = ["S_Hard_Skill", 
          "E_Hard_Skill",
          "S_Soft_Skill",
          "E_Soft_Skill",
          "S_Company_Name",
          "E_Company_Name",
          "S_Years_Experince",
          "E_Years_Experince",
          "S_Important_Dates",
          "E_Important_Dates",
          "S_Person",
          "E_Person",
          "S_location",
          "E_location",
          "S_perks",
          "E_perks"
          ]

walker(".\\raw data", queue_filename)
remover = []
for fo in open(queue_filename, "r"):
    file_names.append(fo[:-1])

for f in file_names:
    temp = f.split("!")
    if len(temp) >= 2:
       remover.append(temp[0])
       remover.append(f)

for l in remover:
    file_names.remove(l)

def cutup(input):
    temp_list = []
    fs = True
    text = re.sub("\n", " ", input)
    text = re.sub("  ", " ", text)
    text = re.sub(",", " ,", text)
    text = re.sub("'", " '", text)
    
    temp_list.append(text)        
    


    return temp_list

for i in file_names:
    f = open(i,'r',encoding="UTF-8")
    str_list.append(f.read())
    f.close


def splitting(stringly):
    real_list = []
    encoding_list = []

    for n in stringly:
        temp = n.split(" ")
        for j in temp:
            if j.find("|") >= 0 :
                temp2 = j.split("|")
                real_list.append(temp2[0])
                encoding_list.append(temp2[1])
            else:
                real_list.append(j)
                encoding_list.append("O")
    return [real_list, encoding_list]

for i in range(len(file_names)):
    str_list[i] = cutup(str_list[i])

# str_list[0] = cutup(str_list[0])

    # print(".\\raw data" + "\\" + file_names[i].split("\\")[-1]+ "!" + "done.txt")
    temp = splitting(str_list[i])
    name = file_names[i].split("\\")[-1]

    fb = open(".\\pre csv data\\" + name, "w", encoding="UTF-8")

    for k in range(2):
        for j in temp[k]:
            fb.write(j+" ")
        fb.write("|")
    fb.close()

    fc = open(".\\raw data" + "\\" + name + "!" + "done.txt","w")
    fc.write("d")    
    fc.close()