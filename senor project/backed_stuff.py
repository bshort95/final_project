
def display(text, mask):
    kp_list = {}
    
    
    text_list = text.split(" ")
    mask_list = mask.split(" ")
    
    display_string = ""
   

    for i in range(len(text_list)):
        if mask_list[i] != "O":     
            if mask_list[i][2:] in kp_list:
                kp_list[mask_list[i][2:].strip()].append(mask_list[i][:2] + text_list[i])
            else:
                kp_list[mask_list[i][2:].strip()] = [mask_list[i][:2] + text_list[i]]
    
    for i in kp_list:
        display_string = display_string + "-" + i + "\n\n"
        temp_str = ""
    
        for j in kp_list[i]:
            
            if j != "" and j[0] == 'S':
                if j[2:] != "," and j[2:] != " "and j[2:] and temp_str != "":
                    display_string = display_string + temp_str + "\n"
                    temp_str = ""
            
            if j[2:] != "," and j[2:] != " ":    
                temp_str = temp_str + j[2:] + " "
        display_string = display_string + temp_str + "\n" + "-----------"+ "\n"
            
    return display_string

# print(display(text, mask))

