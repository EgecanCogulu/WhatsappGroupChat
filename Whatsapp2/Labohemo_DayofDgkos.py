# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 12:45:06 2020

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

def date_converter(day):
    month,day,year=day.split("/")
    month=int(month)
    day=int(day)
    return (int((month-1)*30.5+day))
    

filename=r"C:\Users\Egecan\Desktop\labohemo.txt"

file=open(filename,'r', encoding="utf8") 
# text=file.read()
lines=file.readlines()

file.close()





dgko_keywords=["Dgko","dgko","Ko ", "KO ", "doğdun"]   
dgko_dates={}

for (i,line) in enumerate(lines):
    start=line.find(" - ")
    stop=line.find(": ")
    person=line[start+3:stop]
    comma=line.find(", ")
    
    if any(x in line for x in dgko_keywords):
        try:
            dgko_dates[line[:comma]]+=1
        except KeyError:
            dgko_dates[line[:comma]]=1

dgko_dates.pop("4/25/20")
dgko_dates.pop("5/22/20")
dgko_dates.pop("6/4/20")
dgko_dates.pop("11/25/20")

dgko_dates["8/20/20"]=dgko_dates["8/20/20"]+dgko_dates["8/21/20"]
dgko_dates.pop("8/21/20")

dgko_dates["10/29/20"]=dgko_dates["10/29/20"]+dgko_dates["10/28/20"]
dgko_dates.pop("10/28/20")

dgko_dates["5/18/20"]=dgko_dates["5/18/20"]+dgko_dates["5/17/20"]
dgko_dates.pop("5/17/20")

dgko_dates["5/4/20"]=20
dgko_dates["5/5/20"]=22

lists = dgko_dates.items() # sorted by key, return a list of tuples

daylist, numberofdgkos = zip(*lists)

daylist=list(daylist)
numberofdgkos=list(numberofdgkos)

people=["Cemil","Delibo","Ibozeyd","Şizo","Alihan","Zalaman"]
dates=["4 Nisan","15 Nisan","4 Mayıs","5 Mayıs","18 Mayıs","31 Temmuz","10 Ağustos","20 Ağustos","24 Ağustos","24 Eylül","28 Eylül","8 Ekim","13 Ekim",
        "29 Ekim","1 Kasım","23 Kasım","28 Kasım","4 Aralık","24 Aralık"]
my_cmap = cm.get_cmap("viridis")
my_norm = Normalize(vmin=10,vmax=20)
fig,ax=plt.subplots()
plt.bar(dates,numberofdgkos,color=my_cmap(my_norm(numberofdgkos)), edgecolor='black')
ax.set_xticklabels(dates, rotation=85,horizontalalignment="center")
plt.title("En Çok Kutlanan Doğum Günleri",size=13)
plt.ylabel("Mesaj Sayısı",size=13)
plt.xlabel("Gün",size=13)
plt.tight_layout()
plt.savefig(r"C:\Users\Egecan\Desktop\output\Dgko Gunleri.png",dpi=600)


# days=np.arange(365)
# dgko_number=np.zeros(365)

# for index,day in enumerate(daylist):
#     dgko_number[date_converter(day)]=numberofdgkos[index]
    
    
    
# fig,ax=plt.subplots()
# plt.bar(days,dgko_number,color="k")
# # ax.set_xticklabels(daylist, rotation=90,horizontalalignment="center")