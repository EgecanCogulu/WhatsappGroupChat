# -*- coding: utf-8 -*-
"""
Created on Fri May  1 23:48:55 2020

@author: Egecan
"""


# -*- coding: utf-8 -*-
"""
Created on Fri May  1 23:34:33 2020

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

import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


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
        
def remover(message):
    if ("http" in message) or ("https" in message) or ("Media" in message) or ("omitted" in message) or len(message)<4:
        return True
    else:
        return False

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
        'Koko', 'Bambam', 'Mert Arin', 'Taylan','Emre Çarkcı', 'Dai', 'Alihan']


instancedict = {person: bohem(person) for person in people}


for (i,line) in enumerate(lines[:]):
    start=line.find(" - ")
    stop=line.find(": ")
    person=line[start+3:stop]

    if person in people:
        instancedict[person].messages.append(line[stop+2:-1])
        
messages={}        
for person in people:
    messages[person]=sum(len(i) for i in instancedict[person].messages)/len( instancedict[person].messages)



lists = sorted(messages.items(), key=lambda kv: kv[1], reverse=True) # sorted by key, return a list of tuples

namelist, numberofmessages = zip(*lists)

namelist=list(namelist)
numberofmessages=list(numberofmessages)


# numberofmessages[i1]=numberofmessages[i1]+numberofmessages[i2]

# namelist.pop(i2)   
# numberofmessages.pop()        
#####################################
#Customize names:
    
# namelist[namelist.index("Ali Kavakdere")]="Ali"
# namelist[namelist.index("Mert Arin 141")]="Mert"    
# namelist[namelist.index("Emre Çarkcı")]="Çarkcı"  
# namelist[namelist.index("Alp Yurtsever")]="Optik" 
# namelist[namelist.index("Semih Anıl")]="Semih" 
# namelist[namelist.index("Cem Alcinkaya")]="Cem Alço"
# namelist[namelist.index("Gaşşar")]="Selim"
###################################



my_norm =SymLogNorm(linthresh=0.03, linscale=0.03, base=2,vmin=22, vmax=45)

def generateWC(name,cmp):
    allmessages=instancedict[name].messages
    combinedstr=" ".join(allmessages)
    allmessages=combinedstr.split()
    allmessages2 = [message for message in allmessages if not remover(message)]
    combinedstr=" ".join(allmessages2)
    wordcloud = WordCloud(width=1000, height=500,max_font_size=160, max_words=100, background_color="black",colormap=cmp).generate(combinedstr)
    
    plt.figure( figsize=(20,10))
    plt.imshow(wordcloud, interpolation="Bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(r"C:\Users\Egecan\Desktop\Bohemo Analiz\WCs\New\\"+str(name)+".png",dpi=300)
     

    return (combinedstr)


cmaps= ['plasma', 'inferno', 'magma',
        
        
        'Greens', 'Oranges', 'Reds',
        'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
        'GnBu', 'PuBu', 'YlGnBu', 'BuGn', 'YlGn',
        
        'PiYG', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
        'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr',
        
        'Pastel1', 'Pastel2', 'Paired', 'Accent',
        'tab20b', 'tab20c'
        ]

for person in instancedict:
    index=np.random.randint(len(cmaps))
    generateWC(messages[person],cmaps[index])
    
    