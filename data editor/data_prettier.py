import pandas as pd


legend = ['S_Misc_Info',
'E_Misc_Info',
'S_resp',
'E_resp',
'S_Hard_Skill',
'E_Hard_Skill',
'S_Soft_Skill',
'E_Soft_Skill',
'S_Company_Name',
'E_Company_Name',
'S_Years_Experince',
'E_Years_Experince',
'S_Important_Dates',
'E_Important_Dates',
'S_Person',
'E_Person',
'S_location',
'E_location',
'S_perks',
'E_perks',
'S_degree',
'E_degree']

df = pd.read_csv('csv data\data.csv')
df.values

