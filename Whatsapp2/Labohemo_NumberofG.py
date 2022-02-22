
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:03:02 2020

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
        'Koko', 'Bambam', 'Mert Arin', 'Taylan',
        'Emre Çarkcı', 'Dai', 'Alihan']



instancedict = {person: bohem(person) for person in people}


for (i,line) in enumerate(lines[:]):
    start=line.find(" - ")
    stop=line.find(": ")
    person=line[start+3:stop]

    if person in people:
        instancedict[person].messages.append(line[stop+2:-1])


        
messages_per_G={} 
Gs={}       
for person in people:
    Gs[person]=instancedict[person].messages.count("G")
    messages_per_G[person]=instancedict[person].messages.count("G")/len(instancedict[person].messages)

lists = sorted(Gs.items(), key=lambda kv: kv[1], reverse=True) # sorted by key, return a list of tuples
namelist, numberofGs = zip(*lists)

namelist=list(namelist)
numberofGs=np.asfarray(numberofGs)


# lists = sorted(messages_per_G.items(), key=lambda kv: kv[1], reverse=True) # sorted by key, return a list of tuples
# namelist, messages_per_Gs = zip(*lists)

# namelist=list(namelist)
# messages_per_Gs=np.asfarray(messages_per_Gs)
       
##########################
#Customize names:
    
namelist[namelist.index("Mert Arin")]="Mert"    
namelist[namelist.index("Emre Çarkcı")]="Emre"  


my_cmap = cm.get_cmap('RdYlBu')
my_norm =Normalize(vmin=0, vmax=200)
fig,ax=plt.subplots()


plt.ylabel("G Sayısı",size=15)
plt.title("Toplam 'G' Sayısı: %d" %sum(numberofGs))
# plt.xlabel("Bohem Kişi")
plt.bar(namelist,numberofGs,color=my_cmap(my_norm(numberofGs)),  edgecolor='black')
ax.set_xticklabels(namelist, rotation=90,horizontalalignment="center")
plt.tight_layout()
plt.savefig(r"C:\Users\Egecan\Desktop\Atılan Toplam G.png",dpi=600)



lists = sorted(messages_per_G.items(), key=lambda kv: kv[1], reverse=True) # sorted by key, return a list of tuples
namelist, messages_per_Gs = zip(*lists)

namelist=list(namelist)
messages_per_Gs=np.asfarray(messages_per_Gs)*100

my_cmap = cm.get_cmap('RdBu_r')
my_norm =LogNorm(vmin=2, vmax=35)

fig,ax=plt.subplots()
plt.ylabel("G/Mesaj (%)",size=15)
plt.title("G/Mesaj Yüzdesi")
plt.bar(namelist,messages_per_Gs,color=my_cmap(my_norm(messages_per_Gs)),  edgecolor='black')
ax.set_xticklabels(namelist, rotation=90,horizontalalignment="center")
plt.tight_layout()
plt.savefig(r"C:\Users\Egecan\Desktop\Toplam GvsMesaj.png",dpi=600)



