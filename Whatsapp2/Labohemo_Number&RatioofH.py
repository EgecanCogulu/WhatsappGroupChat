# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 11:46:25 2020

@author: Egecan
"""


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
        'Koko', 'Bambam', 'Mert Arin',
        'Emre Çarkcı', 'Dai', 'Alihan']



instancedict = {person: bohem(person) for person in people}


for (i,line) in enumerate(lines[:]):
    start=line.find(" - ")
    stop=line.find(": ")
    person=line[start+3:stop]

    if person in people:
        instancedict[person].messages.append(line[stop+2:-1])


        
messages_per_H={} 
Hs={}       
for person in people:
    Hs[person]=instancedict[person].messages.count("H")
    messages_per_H[person]=instancedict[person].messages.count("H")/len(instancedict[person].messages)

lists = sorted(Hs.items(), key=lambda kv: kv[1], reverse=True) # sorted by key, return a list of tuples
namelist, numberofHs = zip(*lists)

namelist=list(namelist)
numberofHs=np.asfarray(numberofHs)


# lists = sorted(messages_per_G.items(), key=lambda kv: kv[1], reverse=True) # sorted by key, return a list of tuples
# namelist, messages_per_Gs = zip(*lists)

# namelist=list(namelist)
# messages_per_Gs=np.asfarray(messages_per_Gs)
       
##########################
#Customize names:
    
namelist[namelist.index("Mert Arin")]="Mert"    
namelist[namelist.index("Emre Çarkcı")]="Emre"  


my_cmap = cm.get_cmap('RdYlBu')
my_norm =Normalize(vmin=0, vmax=90)
fig,ax=plt.subplots()

plt.ylabel("H Sayısı",size=15)
plt.title("Toplam 'H' Sayısı: %d" %sum(numberofHs))
# plt.xlabel("Bohem Kişi")
plt.bar(namelist,numberofHs,color=my_cmap(my_norm(numberofHs)),  edgecolor='black')
ax.set_xticklabels(namelist, rotation=90,horizontalalignment="center")
ax.set_ylim(0,95)
ax2 = ax.twinx()
ax2.set_ylabel('Tüm "H" lere Oranı (%)',fontsize=13)
fullscale=np.round(95/sum(numberofHs),2)*100
ax2.set_yticks(np.asfarray([0,0.2,0.4,0.6,0.8,1])*fullscale)
plt.tight_layout()
plt.savefig(r"C:\Users\Egecan\Desktop\output\H.png",dpi=600)



lists = sorted(messages_per_H.items(), key=lambda kv: kv[1], reverse=True) # sorted by key, return a list of tuples
namelist, messages_per_Hs = zip(*lists)

namelist=list(namelist)
messages_per_Hs=np.asfarray(messages_per_Hs)*100


namelist[namelist.index("Mert Arin")]="Mert"    
namelist[namelist.index("Emre Çarkcı")]="Emre"

my_cmap = cm.get_cmap('RdBu_r')
my_norm =LogNorm(vmin=0.5, vmax=9)

fig,ax=plt.subplots()
plt.ylabel("H/Mesaj (%)",size=15)
plt.title("H/Mesaj Yüzdesi")
plt.bar(namelist,messages_per_Hs,color=my_cmap(my_norm(messages_per_Hs)),  edgecolor='black')
ax.set_xticklabels(namelist, rotation=90,horizontalalignment="center")
plt.tight_layout()
plt.savefig(r"C:\Users\Egecan\Desktop\output\H Mesaj Oranı.png",dpi=600)



