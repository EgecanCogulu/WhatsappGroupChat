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
        'Delibo', 'Ibozeyd', 'Canbolat Abi', 'Şopar', 'Egecan', 'Memetcan', 'Çeko', 'Boş', 'Zalaman', 'Dai',
        'Koko', 'Bambam', 'Mert Arin', 'Cem Alço', 'Semih', 'Taylan', 'Eray Er', 'Gaşşar',
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
    messages[person]=len( instancedict[person].messages)


lists = sorted(messages.items(), key=lambda kv: kv[1], reverse=True) # sorted by key, return a list of tuples

namelist, numberofmessages = zip(*lists)

namelist=list(namelist)
numberofmessages=list(numberofmessages)

      
##########################
#Customize names:
    
# namelist[namelist.index("Ali Kavakdere")]="Ali"
# namelist[namelist.index("Mert Arin 141")]="Mert"    
# namelist[namelist.index("Emre Çarkcı")]="Çarkcı"  
# namelist[namelist.index("Alp Yurtsever")]="Optik" 
# namelist[namelist.index("Semih Anıl")]="Semih" 
# namelist[namelist.index("Cem Alcinkaya")]="Cem Alço"
# namelist[namelist.index("Gaşşar")]="Selim"
namelist[namelist.index("Eray Er")]="Eray"
############################

my_cmap = cm.get_cmap('RdYlGn')
my_norm =SymLogNorm(linthresh=0.03, linscale=0.03, base=2,vmin=175, vmax=6000)
fig,ax=plt.subplots()

plt.ylabel("Mesaj Sayısı",size=15)
plt.title("Toplam Mesaj: %2d" %(sum(numberofmessages)))
# plt.xlabel("Bohem Kişi")
plt.bar(namelist,numberofmessages,color=my_cmap(my_norm(numberofmessages)),  edgecolor='black')
ax.set_xticklabels(namelist, rotation=90,horizontalalignment="center")
ax.set_ylim(0,5900)
ax2 = ax.twinx()
ax2.set_ylabel('Tüm Mesajlara Oranı (%)',fontsize=13)
fullscale=np.round(5900/sum(numberofmessages),2)*100
ax2.set_yticks(np.asfarray([0,0.2,0.4,0.6,0.8,1])*fullscale)
# ax2.set_yticklabels(np.asfarray([0,2.5,5,7.5,10,12.5]))


plt.tight_layout()
plt.savefig(r"C:\Users\Egecan\Desktop\output\Mesaj Toplam.png",dpi=600)



