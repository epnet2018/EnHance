#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  2018.03 version by ep_net
#  

#����������
#����Ŀ¼�ļ�
eqmenu='DHB197020152.01998.EQT'
#�����ļ�������䶯
netlist=".\\plot\\netlist.txt"
#ɨ�������Զ�Ϊ��λ��˫����
#��ֱ���
vinterval=2.0
#ˮƽ���
linterval=2.0
#������ǿ��ֵ����,���������ڣ�����������
num=100

#�������ý���
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

#��ʾͼƬ

#�������ڼ��㣬��ǰ���ڵ������ͷ�,��6��������� checkdate��ʽ 19710324154500
def calEnergy(checkdate,quakemenu,slat,elat,slon,elon):
	print(checkdate);
	
	#detester = ��2017-01-01' �ַ���ת��������
	#�������
	cdate = datetime.strptime(checkdate,'%Y%m%d%H%M%S')
	#����ǰ������
	sdate = cdate-timedelta(days=1095)
	#date = datetime.now()
    #������ת���ַ���
	#detester = date.strftime(��%Y-%m-%d')
	
	checkdate=cdate.strftime('%Y%m%d%H%M%S')
	print(cdate.year)
	print(sdate.year)

	ldate=[]
	llat=[]
	llon=[]
	lmag=[]
	ldep=[]
	lyear=[]
		
	#eqt��ȡ����
	with open(eqmenu) as file_object:
		lines = file_object.readlines()
	#for line in lines:
		#�������ǰ�������
		#if(datetime.strptime(line[1:15],'%Y%m%d%H%M%S')>sdate and datetime.strptime(line[1:15],'%Y%m%d%H%M%S')<cdate )
				#ldate.append(line[1:15])
				#���
				#lyear.append(line[1:5])
				#linea[2] lat
				#llat.append(line[15:21])
				#linea[3][0:6] lon
				#llon.append(line[21:28])
				#linea[3][7:10] mag
				#lmag.append(line[28:33])
				#linea[4] dep
				#ldep.append(line[34:38])
	#while(i<=latmax):
	#j=lonmin
	#while(j<=lonmax):


			
	return;	
	
ldate=[]
llat=[]
llon=[]
lmag=[]
ldep=[]
lyear=[]


	
	
#eqt��ȡ����
with open(eqmenu) as file_object:
	lines = file_object.readlines()
#lines ������ȫ����������
#��������֡
df=pd.DataFrame()
#��һ��ѭ������÷�Χ���� ����eqt����Ŀ¼
for line in lines:
	#linea=line.split(' ',4)
	#linea[1] date
	ldate.append(line[1:15])
	#���
	lyear.append(line[1:5])
	#linea[2] lat
	llat.append(line[15:21])
	#linea[3][0:6] lon
	llon.append(line[21:28])
	#linea[3][7:10] mag
	lmag.append(line[28:33])
	#linea[4] dep
	ldep.append(line[34:38])
	#df.append({'date':line[1:15],'lat':line[15:21],'lon':line[21:28],'mag':line[28:33],'dep':line[34:38]},ignore_index=True)
	#dicts=[{'date': line[1:15],'lat': line[15:21],'lon': line[21:28],'mag': line[28:33],'dep': line[34:38]}]
	#df=df.append(dicts, ignore_index=True)
	#���������
	#ɨ��Ŀ¼�����С������Ϊɨ��߽�
	#print(max(linea[2]))
#eqt��ȡ����


#print(max(llat))
#print(min(llat))
#print(max(llon))
#print(min(llon))
#print(max(lyear))
#print(min(lyear))
print(df)
#
#���������
latmin=float(min(llat))
latmax=float(max(llat))
lonmin=float(min(llon))
lonmax=float(max(llon))
yearmax=int(max(lyear))
yearmin=int(min(lyear))
#�����С������

#��������ļ�������ɾ��
if(os.path.exists(netlist)):
	os.remove(netlist)
	
#����ÿ������4��������꣬��8��������ʽ lat1,lon1;lat2,lon2;lat3,lon3;lat4,lon4 �����浽�ļ���
#�������Ͻ����꣬���Բ���Ҫ�ӷָ���

#�ȼ��㰴����ͷ����ʵ�

#�����Ѿ��õ���ÿ������ͷ���
i=latmin
#while(i<=latmax+linterval):
while(i<=latmax):
	j=lonmin
	while(j<=lonmax):
		print("%.2f,%.2f;%.2f,%.2f;%.2f,%.2f;%.2f,%.2f"%(i,j,i+linterval,j,i+linterval,j+vinterval,i,j+vinterval))
		#��¼ÿ��������ĵ�����
		eqcount=0
		#�������ڻ�ͼ
		Energy=[]
		Edates=[]
		EnergySum=0.00
		#��ǰ��ݣ�����ÿ��ÿ������ͷ���
		YearE=""
	
		#������Ŀ¼
		for line in lines:
			#linea=line.split(' ',4) #eqt�����ÿո�ֶΣ��𼶴�������ռλ
			#linea[1] date
			#linea[2] lat
			#linea[3][0:6] lon
			#linea[3][6:10] mag
			#linea[4] dep
						
			#������������ã���һ��������11.8+1.5M ����������Y��������X��ʱ��
			#�������
			#print(line[1:5])
			YearE=line[1:5]
			#�жϵ���֪���ڷ�Χ��
			if(check_point.check_point(line[15:21],line[21:28],i,j,vinterval,linterval)):
				eqcount+=1
				print(line[28:33].strip())
				#float('%.2f' % a)
				#print(round(1.5*float(line[28:33].strip()),2))
				#print(line[1:15])	
				
					
				#��ǰ�ͷ���
				EnergySum=EnergySum+1.5*float(line[28:33].strip())+11.8
				calEnergy(line[1:15],1,1,1,1,1)
				#���ڣ�line[1:15]
				#��Ҫ����ǰ3���ƽ���ͷ���
				#����ǰ3��ƽ��Ƶ�Σ���ǰ��Ƶ��
				#

				
				#���ͷ���������ǰ����ƽ���ͷ������������ϣ�����ÿ��������ֵ䣬ֻ��һ��
				#��������ͷ���
				#line[1:4] ���
				#dtstr = '19720212033900' #'2014-02-14 21:32:12'
				#datetime.strptime(dtstr, "%Y-%m-%d %H:%M:%S").date()	
				
									
			
				#���뵽��ͼ����
				Energy.append(EnergySum)
				Edates.append(line[1:15])
				
				# 1.��������������Ӧ���ͷ����߳�������̬�������ͷ���������ǰ����ƽ���ͷ������������ϡ�
				
				# 2��Ӧ���ͷż���ʱ�����ٳ���һ�����ϣ���ô��Ӧ���ͷų�����1��ǰ���ͷ����Ѿ���3��ƽ���ͷ�����2�����ϣ�

				# 3����Ӧ������ͷ��ڼ䣬��������Ƶ��Ҳ���ִ���ͬ��������Ƶ��һ��Ӧ��ǰ����ƽ��ֵ2�����ϡ�
				
			#����Ƶ�����ߵ������ж��㷨
			#today = datetime.now()  
			#dates = [today + timedelta(days=i) for i in range(10)]  
			#values = [random.randint(1, 20) for i in range(10)]  
			#values.append(11.8+1.5*float(linea[3][7:10]))
			#dates.append(time.strptime(linea[1], '%Y%m%d%H%M%S'))	
	
	    #����������������Ѿ��������Ƿ�������ǿ�������жϣ�ֻ�жϵ�ǰʱ���Ƿ�������ǿ�����һ������
	    
	    #һ������һ���������ͼ
		plt.plot(Edates, Energy)
		plt.ylabel('E')
		plt.xlabel('time')
		#plt.gca().xaxis.set_major_formatter(mdate.DateFormatter('%Y'))
		#plt.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))#����ʱ���ǩ��ʾ��ʽ
		#plt.show()
		plt.savefig("net"+str(i)+str(j)+".jpg")  
		plt.close()
		#print(Edates)		
		if eqcount>num:
			with open(netlist,'a') as file_object:
				file_object.write("%.2f,%.2f;%.2f,%.2f;%.2f,%.2f;%.2f,%.2f %d\n"%(i,j,i+linterval,j,i+linterval,j+vinterval,i,j+vinterval,eqcount))	

		#����������߽���	
		j+=vinterval
		#��ͼ ������ֵ�ĲŻ�ͼ
		#pylab.plot_date(pylab.date2num(dates), values, linestyle='-')  
		#text(17, 277, u'')  
		#xtext = xlabel('time (s)')  
		#ytext = ylabel('E')  
		#ttext = title('E-T')  
		#grid(True)  
		#setp(ttext, size='large', color='r')  
		#setp(text, size='medium', name='courier', weight='bold',color='b')  
		#setp(xtext, size='medium', name='courier', weight='bold', color='g')  
		#setp(ytext, size='medium', name='helvetica', weight='light', color='b')  
		#savefig('simple_plot.png')  
		#filename ="plot"+str(i)+str(j)
		#savefig(filename)  
		#show() 

	i+=linterval
#for latmin in range(latmin,latmax,linterval):
	#print(latmin)


#����������

#��ͼ   pip install Pillow ��ʾͼƬ
os.chdir(".\\plot\\")
os.system("start .\\plot.bat")
os.getcmd()

#��ʾͼƬ
import matplotlib.pyplot as plt
from PIL import Image
img=Image.open('.\\plot\\netlist.jpg')
#img=Image.open('D:\\DizhenjvDev\\EnHancePy\\plot\\netlist.jpg')
plt.figure("restut")
plt.imshow(img)
plt.show()





