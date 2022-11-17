import pandas as pd
import numpy as np
import csv

ori_data=csv.reader(open('C:\\Users\\归零\\Desktop\\need_data.csv'))##原始数据

##以字典的形式重建csv
country=['A','B','C','A','B','C']
year=[1999,1999,1999,2000,2000,2000]
cases=['0.7k','37k','212k','2k','80k','213k']

frame_data=pd.DataFrame({'country':country,'year':year,'cases':cases})##字典的key值对应csv中的列名
frame_data.to_csv('C:\\Users\\归零\\Desktop\\new_data.csv',index=False,sep=',')
print(frame_data)