# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 14:22:55 2020

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
        
media={}
media_per_message={}       
for person in people:

    media[person]=instancedict[person].messages.count("<Media omitted>")

    media_per_message[person]=media[person]/len(instancedict[person].messages)
    



lists = sorted(media.items(), key=lambda kv: kv[1], reverse=True) # sorted by key, return a list of tuples

namelist, numberofmedia = zip(*lists)

namelist=list(namelist)
numberofmedia=list(numberofmedia)


     
##########################
#Customize names:
    

namelist[namelist.index("Mert Arin")]="Mert"    
namelist[namelist.index("Emre Çarkcı")]="Emre"  
namelist[namelist.index("Semih Anıl")]="Semih" 


my_cmap = cm.get_cmap('RdYlBu_r')

my_norm =SymLogNorm(linthresh=0.03, linscale=0.03, base=2,vmin=5, vmax=265)
fig,ax=plt.subplots()


plt.ylabel("Foto&Video Sayısı",size=15)
plt.title("Toplam Fotoğraf&Video: %d" %(sum(numberofmedia)))
# plt.xlabel("Bohem Kişi")
plt.bar(namelist,numberofmedia,color=my_cmap(my_norm(numberofmedia)),  edgecolor='black')
ax.set_xticklabels(namelist, rotation=90,horizontalalignment="center")
ax.set_ylim(0,290)
ax2 = ax.twinx()
ax2.set_ylabel('Tüm Foto&Videolara Oranı (%)',fontsize=13)
fullscale=np.round(290/sum(numberofmedia),2)*100
ax2.set_yticks(np.asfarray([0,0.2,0.4,0.6,0.8,1])*fullscale)
plt.tight_layout()
plt.savefig(r"C:\Users\Egecan\Desktop\output\Medya.png",dpi=600)




lists = sorted(media_per_message.items(), key=lambda kv: kv[1], reverse=True) # sorted by key, return a list of tuples
namelist, media_per_message = zip(*lists)

namelist=list(namelist)
media_per_message=np.asfarray(media_per_message)*100

namelist[namelist.index("Mert Arin")]="Mert"    
namelist[namelist.index("Emre Çarkcı")]="Emre"  
namelist[namelist.index("Semih Anıl")]="Semih" 

my_cmap = cm.get_cmap('RdBu_r')
my_norm =LogNorm(vmin=0.5, vmax=16)

fig,ax=plt.subplots()
plt.ylabel("Foto&Video/Mesaj (%)",size=15)
plt.title("Foto&Video/Mesaj Yüzdesi")
plt.bar(namelist,media_per_message,color=my_cmap(my_norm(media_per_message)),  edgecolor='black')
ax.set_xticklabels(namelist, rotation=90,horizontalalignment="center")
plt.tight_layout()
plt.savefig(r"C:\Users\Egecan\Desktop\output\Medya Mesaj Orani.png",dpi=600)

