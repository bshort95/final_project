import torch
from transformers import BertTokenizerFast, BertModel, BertForTokenClassification
import re
from backed_stuff import display
import tkinter as tk
from tkinter import *
from tkinter import ttk

"prep to load model in"
"============================================================"


unique_labels = {'S_location',
                 'E_Hard_Skill',
                 'S_Hard_Skill',
                 'S_Misc_Info',
                 'S_Soft_Skill',
                 'E_Company_Name',
                 'S_Years_Experince',
                 'E_Important_Dates',
                 'S_perks',
                 'E_Soft_Skill',
                 'E_degree',
                 'S_Company_Name',
                 'S_resp',
                 'S_degree',
                 'E_resp',
                 'E_Years_Experince',
                 'O',
                 'E_location',
                 'S_Important_Dates',
                 'E_perks',
                 'E_Misc_Info'}

labels_to_ids = {k: v for v, k in enumerate(sorted(unique_labels))}
ids_to_labels = {v: k for v, k in enumerate(sorted(unique_labels))}

class BertModel1(torch.nn.Module):

    def __init__(self):

        super(BertModel1, self).__init__()

        self.bert = BertForTokenClassification.from_pretrained('bert-base-cased', num_labels=len(unique_labels))

    def forward(self, input_id, mask, label):

        output = self.bert(input_ids=input_id, attention_mask=mask, labels=label, return_dict=False)

        return output


tokenizer = BertTokenizerFast.from_pretrained('bert-base-cased')
pickled_model = torch.load('model3.pt',map_location=torch.device('cpu'))
label_all_tokens = True

def align_word_ids(texts):

    tokenized_inputs = tokenizer(texts, padding='max_length', max_length=512, truncation=True)

    word_ids = tokenized_inputs.word_ids()

    previous_word_idx = None
    label_ids = []

    for word_idx in word_ids:

        if word_idx is None:
            label_ids.append(-100)

        elif word_idx != previous_word_idx:
            try:
                label_ids.append(1)
            except:
                label_ids.append(-100)
        else:
            try:
                label_ids.append(1 if label_all_tokens else -100)
            except:
                label_ids.append(-100)
        previous_word_idx = word_idx

    return label_ids


def evaluate_one_text(model, sentence):

    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")

    if use_cuda:
        model = model.cuda()

    text = tokenizer(sentence, padding='max_length', max_length = 512, truncation=True, return_tensors="pt")

    mask = text['attention_mask'].to(device)
    input_id = text['input_ids'].to(device)
    label_ids = torch.Tensor(align_word_ids(sentence)).unsqueeze(0).to(device)

    logits = model(input_id, mask, None)
    logits_clean = logits[0][label_ids != -100]

    predictions = logits_clean.argmax(dim=1).tolist()
    prediction_label = [ids_to_labels[i] for i in predictions]
    return sentence + '|' + " ".join(prediction_label)


def cutup(input):
    
    text = re.sub("\n", " ", input)
    text = re.sub("  ", " ", text)
    text = re.sub(",", " ,", text)
    text = re.sub("'", " '", text)
    text = re.sub("|", "", text)
    
    return text.strip()

def cutter(lis):
    bob = lis.split(" ")    
    temp_list= []

    fs = True
    s = 0
    e = 50
    inc = 50
    while fs:
        if e > len(bob)-1:
            e = len(bob)
            fs = False
    
        temp_list.append(" ".join(bob[s:e]))
        s=s + inc 
        e=e + inc

    return temp_list


def predict_text(text):


    clean_text = cutup(text)
    pre_model_chunk = cutter(clean_text)

    temp_text_list = []
    temp_pred_list = []
    for i in pre_model_chunk:
        temp = evaluate_one_text(pickled_model, i).split('|')
        temp_text_list.append(temp[0])
        temp_pred_list.append(temp[1])

    

    final_pred = " ".join(temp_pred_list)

    return clean_text + "|" + final_pred

def funky_boys(text):
    temp = predict_text(text).split("|")

    return display(temp[0], temp[1])



'''vetting'''
"==============================================================="
def is_text_valid(input):
    input = input.strip()

    if input == "": 
        return False
    if input.isdigit():
        return False

    
    return True

def get_text_from_path(path):
    temp_string = ""
    print(path.strip())
    try:
        for i in open('.\\' + path.strip(),"r"):
            temp_string += i

    except:
        temp_string =  "file not found"
    
    return temp_string

'''application'''
"================================================================"
explanation = ""
for i in open('exp.txt',"r"):
    explanation += i



win = tk.Tk()

win.geometry("750x750")
win.title("Entities from Listings: Intelligent Job-post Analysis Helper")

def open_popup():
   global explanation
   top= Toplevel(win)
   top.geometry("750x250")
   top.title("explanation window")
   Label(top, text= explanation, font=('Times 12 bold')).pack()

def display_text():
   global m1
   global CheckVar2
   global display_t
   strin = m1.get("1.0",END)
   
   if is_text_valid(strin):
      try:
        if CheckVar2.get() == 0:
            string= funky_boys(strin)
        else:
            string_content = get_text_from_path(strin)
            
            if string_content == "file not found":
                string = string_content
            else:
                string= funky_boys(string_content)
      except:
        string = "something unexpected happened. please, dont break my app"
   
   else:
    string = "not valid input"

   label.delete('1.0',"end")
     
   label.insert('1.0', string)

   
#Initialize a Label to display the User Input
display_t = ""
header_info = Label(win,text="Welcome to ELI", font=("Times 12 bold"),background="#75b8bd").pack()
label=Text(win, width= 65, font=("Times 12 bold"),  background="#86d5dd")
scrollbar = ttk.Scrollbar(win, orient='vertical', command=label.yview)


label['yscrollcommand'] = scrollbar.set


CheckVar2 = IntVar()

m1 = Text( win,  width= 80, height= 15, background="#86d5dd" )

m1.pack()

r1 =  Checkbutton(win, text = "use path", variable = CheckVar2,
                 onvalue = 1, offvalue = 0, height=5,
                 width = 20, bg="#75b8bd", activebackground="#75b8bd")
r1.pack(padx=15)

ttk.Button(win, text= "press to proccess",width= 20, command= display_text).pack(padx=245)
win.configure(bg='#75b8bd')
label.pack()
ttk.Button(win, text= "?", command= open_popup).place( x = win.winfo_screenmmwidth() - 400 , y = 10)

win.mainloop()