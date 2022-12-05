
import os
# ilist = [['Full', 'Job', 'Description', 'Position', 'Overview', 'State', 'Farm', 'Insurance', 'Agent', 'hire', 'their'], ['own', 'employees.', 'State', 'Farm', 'agentsâ€™', 'employees', 'are', 'not', 'employees', 'of', 'State', '21']]

# legend = {1:"bob",2:"joe",3:"sal"}

def gamify(ilist,legend):
    
    still_going = True
    counter = 0
    start = 0 
    coupled = []
    encoded = []
    real = []
    inc = 5
    end = start + inc
    loopy = False
    while still_going:
        fs = True        
        while fs:
            os.system('cls')
            bob = (ilist[counter][start:end])
            print(f"{len(ilist)}:{counter}")
            print(legend)
            print(bob)
            temp = input()

            if (len(temp.split(",")) == len(bob)):
                fs = False
        c = 0
            
        for n in temp.split(","):
            if n.isnumeric():
                real.append(bob[c])
                encoded.append(legend.get(int(n)))
            elif n.find(".")!= -1:
                encoded.append("O")
                if len(n) > 1:
                    real.append(n[:-1])
                else:
                    real.append(bob[c])
            else:
                if n.find("!") != -1:
                    real.append(n.split("!")[0])
                    encoded.append(legend.get(int(n.split("!")[1])))
                else:
                    real.append(n)
                    encoded.append("O")
            c += 1   
        
        
        if end == len(ilist[counter]):
            print("swag")
            
            counter = counter + 1
            start = 0
            end = 0 + inc
            
        if counter == len(ilist):
            break
        
        if end + inc < len(ilist[counter]):
            start = start + inc
            end = end + inc
        else:
            start = start + inc
            end = len(ilist[counter])
        
    return[real, encoded]    
        
# print(gamify(ilist,legend))
