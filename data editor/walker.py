import os

def walker (dir_name, filename):
    
    file_list = []

    for x in os.listdir(dir_name):
            file_list.append(x)

    f = open(filename, "w")

    for n in file_list:
        f.write( dir_name + "\\" + n + '\n')

    f.close()

