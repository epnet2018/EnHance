#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  2018.03 version by ep_net

# test code
#  

eqmenu='DHB197020152.01998.EQT'
netlist=".\\plot\\netlist.txt"
vinterval=2.0
linterval=2.0

num=100

import os
import check_point
import pdb 
import time,datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import dateutil, pylab,random  
import numpy
from pylab import *  
from datetime import datetime,timedelta  
from pandas import Series
import pandas as pd
from pandas import Series,DataFrame

def calEnergy(checkdate,quakemenu,slat,elat,slon,elon):
	print(checkdate);
	cdate = datetime.strptime(checkdate,'%Y%m%d%H%M%S')
	sdate = cdate-timedelta(days=1095)
	checkdate=cdate.strftime('%Y%m%d%H%M%S')
	print(cdate.year)
	print(sdate.year)
	ldate=[]
	llat=[]
	llon=[]
	lmag=[]
	ldep=[]
	lyear=[]

	with open(eqmenu) as file_object:
		lines = file_object.readlines()



			
	return;	
	
ldate=[]
llat=[]
llon=[]
lmag=[]
ldep=[]
lyear=[]


	
	

with open(eqmenu) as file_object:
	lines = file_object.readlines()
df=pd.DataFrame()
for line in lines:
	ldate.append(line[1:15])
	lyear.append(line[1:5])
	llat.append(line[15:21])
	llon.append(line[21:28])
	lmag.append(line[28:33])
	ldep.append(line[34:38])
print(df)
latmin=float(min(llat))
latmax=float(max(llat))
lonmin=float(min(llon))
lonmax=float(max(llon))
yearmax=int(max(lyear))
yearmin=int(min(lyear))
if(os.path.exists(netlist)):
	os.remove(netlist)
i=latmin
#while(i<=latmax+linterval):
while(i<=latmax):
	j=lonmin
	while(j<=lonmax):
		print("%.2f,%.2f;%.2f,%.2f;%.2f,%.2f;%.2f,%.2f"%(i,j,i+linterval,j,i+linterval,j+vinterval,i,j+vinterval))
		eqcount=0

		Energy=[]
		Edates=[]
		EnergySum=0.00

		YearE=""

		for line in lines:

			#print(line[1:5])
			YearE=line[1:5]

			if(check_point.check_point(line[15:21],line[21:28],i,j,vinterval,linterval)):
				eqcount+=1
				print(line[28:33].strip())
		

				EnergySum=EnergySum+1.5*float(line[28:33].strip())+11.8
				calEnergy(line[1:15],1,1,1,1,1)

				Energy.append(EnergySum)
				Edates.append(line[1:15])
		
		plt.plot(Edates, Energy)
		plt.ylabel('E')
		plt.xlabel('time')
		plt.savefig("net"+str(i)+str(j)+".jpg")  
		plt.close()
		if eqcount>num:
			with open(netlist,'a') as file_object:
				file_object.write("%.2f,%.2f;%.2f,%.2f;%.2f,%.2f;%.2f,%.2f %d\n"%(i,j,i+linterval,j,i+linterval,j+vinterval,i,j+vinterval,eqcount))	

		j+=vinterval
	i+=linterval

os.chdir(".\\plot\\")
os.system("start .\\plot.bat")
os.getcmd()

import matplotlib.pyplot as plt
from PIL import Image
img=Image.open('.\\plot\\netlist.jpg')
plt.figure("restut")
plt.imshow(img)
plt.show()





