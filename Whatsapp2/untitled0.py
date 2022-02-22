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

#creating a person object with attributes: name, messages, dates and times
#
class bohem():
    def __init__(self,name):
        self.name=name
        self.messages=[]
        self.dates=[]
        self.times=[]
        
    def add_messages(self,messages):
        messages.append(messages)
        
def time_converter(time):
    time24=int(time.split(":")[0])
    if "PM" in time and time24!=12:
        time24+=12
    if "AM" in time and time24==12:
        time24+=12
    return (time24%24)
    

filename=r"C:\Users\Egecan\Desktop\labohemo.txt"

file=open(filename,'r', encoding="utf8") 
# text=file.read()
lines=file.readlines()

file.close()
people=[]


people=['Çağan', 'Ali', 'Metin', 'Gogo', 'Alp', 'Şizo', 'Eren', 'Palamut', 'Cemil', 
        'Delibo', 'Ibozeyd', 'Canbolat Abi', 'Şopar', 'Egecan', 'Memetcan', 'Çeko', 'Boş', 'Zalaman', 'Dai',
        'Koko', 'Bambam', 'Mert Arin', 'Cem Alço', 'Semih', 'Taylan', 'Eray Er', 'Gaşşar',
        'Emre Çarkcı', 'Dai', 'Alihan']


instancedict = {person: bohem(person) for person in people}


for (i,line) in enumerate(lines):
    start=line.find(" - ")
    stop=line.find(": ")
    person=line[start+3:stop]
    comma=line.find(", ")

    if person in people:
        instancedict[person].messages.append(line[stop+2:-1])
        instancedict[person].dates.append(line[:comma])
        instancedict[person].times.append(line[comma+2:start])
        
messages={}        
for person in people:
    messages[person]=len(instancedict[person].messages)


lists = sorted(messages.items(), key=lambda kv: kv[1], reverse=True) # sorted by key, return a list of tuples

namelist, numberofmessages = zip(*lists)

namelist=list(namelist)
numberofmessages=list(numberofmessages)

      
##########################
#Customize names:
    
# namelist[namelist.index("Ali Kavakdere")]="Ali"
namelist[namelist.index("Mert Arin")]="Mert"    
namelist[namelist.index("Emre Çarkcı")]="Emre"  
# namelist[namelist.index("Alp Yurtsever")]="Optik" 
# namelist[namelist.index("Semih Anıl")]="Semih" 
# namelist[namelist.index("Cem Alcinkaya")]="Cem Alço"
# namelist[namelist.index("Gaşşar")]="Selim"
namelist[namelist.index("Eray Er")]="Eray"
############################

my_cmap = cm.get_cmap('RdYlGn')
my_norm =SymLogNorm(linthresh=0.03, linscale=0.03, base=2,vmin=175, vmax=6000)
fig,ax=plt.subplots()


plt.ylabel("Mesaj Sayısı",size=13)
plt.title("2020 Nisan - Aralık Aylarında Atılan Mesajlar",size=13)
plt.text(20,5500,"Toplam Mesaj: %2d" %(sum(numberofmessages)))
plt.bar(namelist,numberofmessages,color=my_cmap(my_norm(numberofmessages)),  edgecolor='black')
ax.set_xticklabels(namelist, rotation=90,horizontalalignment="center")
plt.tight_layout()
# plt.savefig(r"C:\Users\Egecan\Desktop\output\Atılan Toplam Mesaj.png",dpi=600)



people=['Çağan', 'Ali', 'Metin', 'Gogo', 'Alp', 'Şizo', 'Eren', 'Palamut', 'Cemil', 
        'Delibo', 'Ibozeyd', 'Şopar', 'Egecan', 'Memetcan', 'Çeko', 'Boş', 'Zalaman', 'Dai',
        'Koko', 'Bambam', 'Mert Arin', 'Semih', 'Taylan',
        'Emre Çarkcı', 'Dai', 'Alihan']

messages_per_months=np.zeros(12)
for person in people:
    dates=instancedict[person].dates
    for date in dates:
        messages_per_months[int(date.split("/")[0])-1]+=1
        
messages_per_months=messages_per_months[3:]  

months=["Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]

my_cmap = cm.get_cmap('coolwarm')
my_norm = LogNorm(vmin=3263, vmax=8000)
fig,ax=plt.subplots()
plt.ylabel("Mesaj Sayısı",size=13)
plt.title("En Çok Mesaj Atılan Aylar")
plt.bar(months,messages_per_months,color=my_cmap(my_norm(messages_per_months)),  edgecolor='black')
ax.set_xticklabels(months,horizontalalignment="center")
plt.tight_layout()



messages_per_hour=np.zeros(24)
for person in people:
    times=instancedict[person].times
    for time in times:
        messages_per_hour[time_converter(time)]+=1

# times=["00:00-01:00","01:00-02:00","02:00-03:00","03:00-04:00","04:00-05:00","05:00-06:00","06:00-07:00","07:00-08:00","08:00-09:00","09:00-10:00","10:00-11:00","11:00-12:00",
#        "12:00-13:00","13:00-14:00","14:00-15:00","15:00-16:00","16:00-17:00","17:00-18:00","18:00-19:00","19:00-20:00","20:00-21:00","21:00-22:00",
#        "22:00-23:00","23:00-00:00"]

times=["00:00","01:00","02:00","03:00","04:00","05:00","06:00","07:00","08:00","09:00","10:00","11:00",
       "12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"]

messages_per_hour=np.append(messages_per_hour[-8:],messages_per_hour[:-8])

my_cmap = cm.get_cmap('cividis')
my_norm = Normalize()
fig,ax=plt.subplots()
plt.bar(times,messages_per_hour,color=my_cmap(my_norm(messages_per_hour)), edgecolor='black')
ax.set_xticklabels(times, rotation=80,horizontalalignment="center")
plt.title("En Aktif Saatler",size=13)
plt.ylabel("Mesaj Sayısı",size=13)
plt.xlabel("Saat (GMT+3)",size=13)
plt.tight_layout()


