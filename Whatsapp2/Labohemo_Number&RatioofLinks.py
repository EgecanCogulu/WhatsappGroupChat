# -*- coding: utf-8 -*-
"""
Created on Fri May  1 23:19:46 2020

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
import emoji
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
        
links={}
links_per_message={}
for person in people:
    link_count=0
    for message in instancedict[person].messages:
        if 'https://' in message:
                link_count=link_count+1
    links[person]=link_count
    links_per_message[person]=link_count/len(instancedict[person].messages)
    



lists = sorted(links.items(), key=lambda kv: kv[1], reverse=True) # sorted by key, return a list of tuples

namelist, numberoflinks = zip(*lists)

namelist=list(namelist)
numberofmessages=list(numberoflinks)


# numberofmessages[i1]=numberofmessages[i1]+numberofmessages[i2]

# namelist.pop(i2)   
# numberofmessages.pop()        
##########################
#Customize names:
    

namelist[namelist.index("Mert Arin")]="Mert"    
namelist[namelist.index("Emre Çarkcı")]="Emre"  
namelist[namelist.index("Semih Anıl")]="Semih" 


my_cmap = cm.get_cmap('RdYlBu')

my_norm =SymLogNorm(linthresh=0.03, linscale=0.03, base=2,vmin=5, vmax=265)
fig,ax=plt.subplots()


plt.ylabel("Link Sayısı",size=15)
plt.title("Toplam Link: %d" %(sum(numberoflinks)))
# plt.xlabel("Bohem Kişi")
plt.bar(namelist,numberoflinks,color=my_cmap(my_norm(numberoflinks)),  edgecolor='black')
ax.set_xticklabels(namelist, rotation=90,horizontalalignment="center")
ax.set_ylim(0,230)
ax2 = ax.twinx()
ax2.set_ylabel('Tüm Linklere Oranı (%)',fontsize=13)
fullscale=np.round(230/sum(numberoflinks),2)*100
ax2.set_yticks(np.asfarray([0,0.2,0.4,0.6,0.8,1])*fullscale)
plt.tight_layout()
plt.savefig(r"C:\Users\Egecan\Desktop\output\Link.png",dpi=600)




lists = sorted(links_per_message.items(), key=lambda kv: kv[1], reverse=True) # sorted by key, return a list of tuples
namelist, links_per_message = zip(*lists)

namelist=list(namelist)
links_per_message=np.asfarray(links_per_message)*100

namelist[namelist.index("Mert Arin")]="Mert"    
namelist[namelist.index("Emre Çarkcı")]="Emre"  
namelist[namelist.index("Semih Anıl")]="Semih" 

my_cmap = cm.get_cmap('RdBu_r')
my_norm =LogNorm(vmin=0.5, vmax=9)

fig,ax=plt.subplots()
plt.ylabel("Link/Mesaj (%)",size=15)
plt.title("Link/Mesaj Yüzdesi")
plt.bar(namelist,links_per_message,color=my_cmap(my_norm(links_per_message)),  edgecolor='black')
ax.set_xticklabels(namelist, rotation=90,horizontalalignment="center")
plt.tight_layout()
plt.savefig(r"C:\Users\Egecan\Desktop\output\Link Mesaj Orani.png",dpi=600)

