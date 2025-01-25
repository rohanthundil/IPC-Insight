import nltk
import numpy as np
import pandas as pd


data= pd.read_csv("ipc_dataset.csv")
rows=[]

for i in range(len(data)):
    each_row_tuple= data.loc[i,"Section"], data.loc[i,"Description"], data.loc[i,"Punishment"], data.loc[i,"Bailable/Non-Bailable"]
    
    each_row = list(each_row_tuple)
    rows.append(each_row)
    ##print(data.loc[i,"Section"], data.loc[i,"Description"], data.loc[i,"Punishment"], data.loc[i,"Bailable/Non-Bailable"])
    
for row in rows:
    print(row)