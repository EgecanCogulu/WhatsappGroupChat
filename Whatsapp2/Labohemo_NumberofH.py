# -*- coding: utf-8 -*-
"""
Created on Sat May  2 13:52:40 2020

@author: Egecan
"""




import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib.colors import DivergingNorm
from matplotlib.colors import LogNorm
from matplotlib.colors import SymLogNorm
from matplotlib.colors import Normalize
""" 
Ideas:

World Cloud General/Individual

Posting vs. Time of the Day
Posting vs. Month    

Most "G"
Most Characters
Most Messages/Gs
Most Links
Most Media
Most characters
Most Gaps between Messages
Most Consecutive Gs


"""

class bohem():
    def __init__(self,name):
        self.name=name
        self.messages=[]
        self.dates=[]
        self.times=[]
        
    def add_messages(self,messages):
        messages.append(messages)
        

filename=r"C:\Users\Egecan\Desktop\labohemo.txt"

file=open(filename,'r', encoding="utf8") 
# text=file.read()
lines=file.readlines()

file.close()
people=[]

# for (i,line) in enumerate(lines[:]):
#     start=line.find(" - ")
#     stop=line.find(": ")
#     person=line[start+3:stop]
#     if not (person in people) and start!=-1 and stop!=-1 and person!='' and len(person)<15:
#         people.append(line[start+3:stop])


people=['Çağan', 'Ali', 'Metin', 'Gogo', 'Alp', 'Şizo', 'Eren', 'Palamut', 'Cemil', 
        'Delibo', 'Ibozeyd', 'Şopar', 'Egecan', 'Memetcan', 'Çeko', 'Boş', 'Zalaman', 'Dai',
        'Koko', 'Bambam', 'Mert Arin', 'Semih Anıl', 'Taylan',
        'Emre Çarkcı', 'Dai', 'Alihan']



instancedict = {person: bohem(person) for person in people}


for (i,line) in enumerate(lines[:]):
    start=line.find(" - ")
    stop=line.find(": ")
    person=line[start+3:stop]

    if person in people:
        instancedict[person].messages.append(line[stop+2:-1])
        
messages={}        
for person in people:
    messages[person]=instancedict[person].messages.count("H")



# messages["Dai"]=messages["Dai"]+messages["Dai Usa"]
# del messages["Dai Usa"]



lists = sorted(messages.items(), key=lambda kv: kv[1], reverse=True) # sorted by key, return a list of tuples

namelist, numberofmessages = zip(*lists)

namelist=list(namelist)
numberofmessages=list(numberofmessages)


# numberofmessages[i1]=numberofmessages[i1]+numberofmessages[i2]

# namelist.pop(i2)   
# numberofmessages.pop()        
##########################
#Customize names:
    
namelist[namelist.index("Mert Arin")]="Mert"    
namelist[namelist.index("Emre Çarkcı")]="Emre"  
namelist[namelist.index("Semih Anıl")]="Semih" 


my_cmap = cm.get_cmap('RdYlBu')
my_norm =SymLogNorm(linthresh=0.03, linscale=0.03, base=2,vmin=5, vmax=95)
fig,ax=plt.subplots()


plt.ylabel("H Sayısı",size=15)
plt.title("Toplam 'H' Sayısı: %d" %sum(numberofmessages))
# plt.xlabel("Bohem Kişi")
plt.bar(namelist,numberofmessages,color=my_cmap(my_norm(numberofmessages)),  edgecolor='black')
ax.set_xticklabels(namelist, rotation=90,horizontalalignment="center")
plt.tight_layout()
plt.savefig(r"C:\Users\Egecan\Desktop\Atılan Toplam H.png",dpi=600)