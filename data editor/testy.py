import queue


file_names = []
remover = []
queue_filename = 'queue.txt'

for fo in open(queue_filename, "r"):
    file_names.append(fo[:-1])

for f in file_names:
    temp = f.split("!")
    if len(temp) >= 2:
       remover.append(temp[0])
       remover.append(f)

for l in remover:
    file_names.remove(l)

print(remover)
print(file_names)