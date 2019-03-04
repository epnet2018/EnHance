#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  2018.03 version by ep_net
#  

#参数设置区
#地震目录文件
eqmenu='DHB197020152.01998.EQT'
#网格文件，无需变动
netlist=".\\plot\\netlist.txt"
#扫描间隔，以度为单位，双精度
#垂直间隔
vinterval=2.0
#水平间隔
linterval=2.0
#定义增强阈值个数,单个网格内，地震数下限
num=100

#参数设置结束
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

#显示图片

#按照日期计算，当前日期的能量释放,共6个输入参数 checkdate格式 19710324154500
def calEnergy(checkdate,quakemenu,slat,elat,slon,elon):
	print(checkdate);
	
	#detester = ‘2017-01-01' 字符串转化成日期
	#检测日期
	cdate = datetime.strptime(checkdate,'%Y%m%d%H%M%S')
	#三年前的日期
	sdate = cdate-timedelta(days=1095)
	#date = datetime.now()
    #日期在转成字符串
	#detester = date.strftime(‘%Y-%m-%d')
	
	checkdate=cdate.strftime('%Y%m%d%H%M%S')
	print(cdate.year)
	print(sdate.year)

	ldate=[]
	llat=[]
	llon=[]
	lmag=[]
	ldep=[]
	lyear=[]
		
	#eqt读取程序
	with open(eqmenu) as file_object:
		lines = file_object.readlines()
	#for line in lines:
		#检测日期前三年计算
		#if(datetime.strptime(line[1:15],'%Y%m%d%H%M%S')>sdate and datetime.strptime(line[1:15],'%Y%m%d%H%M%S')<cdate )
				#ldate.append(line[1:15])
				#年份
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


	
	
#eqt读取程序
with open(eqmenu) as file_object:
	lines = file_object.readlines()
#lines 保存了全部地震内容
#定义数据帧
df=pd.DataFrame()
#第一次循环，获得范围参数 处理eqt地震目录
for line in lines:
	#linea=line.split(' ',4)
	#linea[1] date
	ldate.append(line[1:15])
	#年份
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
	#地震处理程序
	#扫描目录最大，最小坐标做为扫描边界
	#print(max(linea[2]))
#eqt读取结束


#print(max(llat))
#print(min(llat))
#print(max(llon))
#print(min(llon))
#print(max(lyear))
#print(min(lyear))
print(df)
#
#打网格程序
latmin=float(min(llat))
latmax=float(max(llat))
lonmin=float(min(llon))
lonmax=float(max(llon))
yearmax=int(max(lyear))
yearmin=int(min(lyear))
#获得最小最大年份

#如果网格文件存在则删除
if(os.path.exists(netlist)):
	os.remove(netlist)
	
#计算每个网格4个点的坐标，共8个数，格式 lat1,lon1;lat2,lon2;lat3,lon3;lat4,lon4 并保存到文件中
#计算左上角坐标，所以不需要加分隔数

#先计算按年的释放量词典

#这里已经得到了每个格的释放量
i=latmin
#while(i<=latmax+linterval):
while(i<=latmax):
	j=lonmin
	while(j<=lonmax):
		print("%.2f,%.2f;%.2f,%.2f;%.2f,%.2f;%.2f,%.2f"%(i,j,i+linterval,j,i+linterval,j+vinterval,i,j+vinterval))
		#记录每个区块里的地震数
		eqcount=0
		#变量用于画图
		Energy=[]
		Edates=[]
		EnergySum=0.00
		#当前年份，计算每年每个格的释放量
		YearE=""
	
		#读地震目录
		for line in lines:
			#linea=line.split(' ',4) #eqt不能用空格分段，震级存在正负占位
			#linea[1] date
			#linea[2] lat
			#linea[3][0:6] lon
			#linea[3][6:10] mag
			#linea[4] dep
						
			#计算蠕变曲线用，第一步，将震级11.8+1.5M 加入纵数组Y，横坐标X是时间
			#地震年份
			#print(line[1:5])
			YearE=line[1:5]
			#判断地震知否在范围内
			if(check_point.check_point(line[15:21],line[21:28],i,j,vinterval,linterval)):
				eqcount+=1
				print(line[28:33].strip())
				#float('%.2f' % a)
				#print(round(1.5*float(line[28:33].strip()),2))
				#print(line[1:15])	
				
					
				#当前释放量
				EnergySum=EnergySum+1.5*float(line[28:33].strip())+11.8
				calEnergy(line[1:15],1,1,1,1,1)
				#日期，line[1:15]
				#需要计算前3年的平均释放量
				#计算前3年平均频次，当前年频次
				#

				
				#年释放量至少是前三年平均释放量的两倍以上，制作每年计算量字典，只算一次
				#按年计算释放量
				#line[1:4] 年份
				#dtstr = '19720212033900' #'2014-02-14 21:32:12'
				#datetime.strptime(dtstr, "%Y-%m-%d %H:%M:%S").date()	
				
									
			
				#加入到画图向量
				Energy.append(EnergySum)
				Edates.append(line[1:15])
				
				# 1.明显上升，整条应变释放曲线呈上跷形态，即年释放量至少是前三年平均释放量的两倍以上。
				
				# 2。应变释放加速时间至少持续一年以上，怎么叫应变释放持续？1年前的释放量已经是3年平均释放量的2倍以上？

				# 3。在应变加速释放期间，该区地震频次也出现大体同步上升，频次一般应是前三年平均值2倍以上。
				
			#计算频度曲线等网格判断算法
			#today = datetime.now()  
			#dates = [today + timedelta(days=i) for i in range(10)]  
			#values = [random.randint(1, 20) for i in range(10)]  
			#values.append(11.8+1.5*float(linea[3][7:10]))
			#dates.append(time.strptime(linea[1], '%Y%m%d%H%M%S'))	
	
	    #这里地震能量序列已经产生，是否显著增强在这里判断，只判断当前时刻是否显著增强，最后一个数据
	    
	    #一个网格画一个蠕变曲线图
		plt.plot(Edates, Energy)
		plt.ylabel('E')
		plt.xlabel('time')
		#plt.gca().xaxis.set_major_formatter(mdate.DateFormatter('%Y'))
		#plt.xaxis.set_major_formatter(mdate.DateFormatter('%Y-%m-%d %H:%M:%S'))#设置时间标签显示格式
		#plt.show()
		plt.savefig("net"+str(i)+str(j)+".jpg")  
		plt.close()
		#print(Edates)		
		if eqcount>num:
			with open(netlist,'a') as file_object:
				file_object.write("%.2f,%.2f;%.2f,%.2f;%.2f,%.2f;%.2f,%.2f %d\n"%(i,j,i+linterval,j,i+linterval,j+vinterval,i,j+vinterval,eqcount))	

		#计算蠕变曲线结束	
		j+=vinterval
		#画图 大于阈值的才画图
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


#网格程序结束

#画图   pip install Pillow 显示图片
os.chdir(".\\plot\\")
os.system("start .\\plot.bat")
os.getcmd()

#显示图片
import matplotlib.pyplot as plt
from PIL import Image
img=Image.open('.\\plot\\netlist.jpg')
#img=Image.open('D:\\DizhenjvDev\\EnHancePy\\plot\\netlist.jpg')
plt.figure("restut")
plt.imshow(img)
plt.show()





