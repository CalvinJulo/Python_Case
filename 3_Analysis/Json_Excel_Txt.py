# coding=utf-8
import pandas as pd
import numpy as np

df1=pd.read_csv('/Users/zcglook/Desktop/寺庙汇总_1.csv')
df2=pd.read_csv('/Users/zcglook/Desktop/邮政编码2.csv')
del df1['Unnamed: 0']
del df2['服务网点名称']
del df2['Unnamed: 0']
del df2['Unnamed: 0.1']
del df2['地址']
del df2['是否办理金融业务']
del df2['备注']
df2.rename(columns={'邮编':'邮政编码'},inplace=True)
#df2.drop_duplicates(inplace=True)
df2.drop_duplicates(inplace=True)
print(df1.tail())
print(df2.tail())

#print(df2.head())
df=pd.merge(df1,df2,how='left',on='邮政编码')

print(df.tail())
#print(df.tail())
df.to_csv('/Users/zcglook/Desktop/寺庙汇总_2.csv')

#df4=pd.merge(df1,df2,how='outer）

#df=pd.read_csv('/Users/zcglook/Downloads/tutorial_flights.csv')
#for i in df.columns: print(i,df.pivot_table(index=i,aggfunc='count',margins=True))
#df.to_csv('/Users/zcglook/Desktop/寺庙
#查询缺失数据
#print(df.isnull().sum())

#填充缺失数据
#df.fillna(value='space',inplace=True)

#查询df基本信息
#df.info()
#df.columns()
#df.index()

# 切片
#table.loc[('佛教'),'count_nonzero']
#table.iloc[1,2]

#排序
#table.sort_values(by=('count_nonzero','邮政编码'),ascending=False)

#透视表
#table=pd.pivot_table(df.fillna(value='space1'),values=['邮政编码'],index=['教别','派别'],aggfunc=[np.count_nonzero],margins=True)

#groupby
#table=df.groupby(by='民宗主管部门').count().sort_values(by='邮政编码',ascending=False)

#print(table)