#빅데이터분석기사실기연습 20211126
import pandas as pd
import numpy as np
import sklearn 
import scipy
import xgboost

# 16번 문제
# 다음은 iris 데이터 세트이다.
# iris 데이터 세트에서 Species가 virginica 인 항목에서
# Sepal.Length가 6보다 크면 1, 아니면 0으로
# 파생 컬럼 Len을 생성 후 Len 컬럼의 sum 값을 구하시오.
data=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/Rdatasets/csv/datasets/iris.csv")
data.columns

vir=data.loc[data['Species']=="virginica"]
vir['Len']=0
vir=vir.reset_index()

for i in range(0,50):
    if vir['Sepal.Length'][i]>6:
        vir['Len'][i]=1
    else:
        vir['Len'][i]=0
        
print(vir['Len'].sum())
# 41

# 17번 문제
# 다음은 airquality 데이터 세트이다. Ozone의 결측값을 
# 없애고 평균 값을 구한 값으로 대체하고, 
# median 값에서 2*IQR을 뺀 값과 
# median 값에서 2*IQR을 더한 값 사이에 존재하는
# Ozone값의 합계를 구하시오.
air=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/Rdatasets/csv/datasets/airquality.csv")
air
ozone_avg=air['Ozone'].mean()

air['Ozone']=air['Ozone'].fillna(ozone_avg)
air['Ozone'].isna().sum()

ozone_med=air['Ozone'].median()
ozone_med
# 42.12

air['Ozone'].describe()
# 25% 21 75% 46

q3=np.percentile(air['Ozone'], 75)
q1=np.percentile(air['Ozone'], 25)
print(q1, q3)
# 21.0 46.0
IQR=q3-q1
print(IQR)
# 25

med_1=ozone_med-(2*IQR)
med_2=ozone_med+(2*IQR)
print(med_1, med_2)
# -7.870689655172413 92.12931034482759

# 첫 번째 풀이
air_1=air.loc[(air['Ozone']>=med_1)&(air['Ozone']<=med_2)]
air_1['Ozone'].sum()
# 5219.7844444

# 두 번재 풀이
air_1=air.loc[air['Ozone']>=med_1]
air_2=air_1.loc[air_1['Ozone']<=med_2]
air_2['Ozone'].sum()
# 5279.7844827586205

print(air_1['Ozone'].sum())
# 5279.784

#18번 문제
# 다음은 marvel 데이터 세트이다. 
# Hair가 "Brown Hair"이고 Eye가
# "Brown Eyes"인 데이터를 훈련 데이터로 추출 했을 때,
# APPEARANCES에서 이상값을 제외한 평균을 구하시오.
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/dc-wikia-data.csv")
df.columns

train=df.loc[(df['HAIR']=="Brown Hair")&(df['EYE']=="Brown Eyes")]
train['HAIR'].unique()
train['EYE'].unique()

# 1st method
train['APPEARANCES'].describe()
q3=26
q1=4
IQR=q3-q1
print(IQR)
#22

# 2nd method
train_2=train.copy()
train_2.dropna(axis=0, inplace=True, subset=["APPEARANCES"])
q3=np.percentile(train_2['APPEARANCES'], 75)
q1=np.percentile(train_2['APPEARANCES'], 25)
IQR=q3-q1
print(IQR)
#22.0

# 1st method
train_3=train_2.loc[(train_2['APPEARANCES']>=q1-(1.5*IQR))&(train_2['APPEARANCES']<=q3+(1.5*IQR))]
print(train_3['APPEARANCES'].mean())
# 12.131868131868131

# 2nd method
train_3=train_2.loc[train_2['APPEARANCES']>=q1-(1.5*IQR)]
train_4=train_3.loc[train_2['APPEARANCES']<=q3+(1.5*IQR)]
print(train_4['APPEARANCES'].mean())
# 12.131868

# 교재 outlier
# 평균에서 1.5*표준편차를 이상치로 간주
a_mean=train_2['APPEARANCES'].mean()
print(a_mean)
# 31.1538
a_std=train_2['APPEARANCES'].std()
print(a_std)
# 99.44596

train_3=train_2.loc[(train_2['APPEARANCES']>=a_mean-(1.5*a_std))&(train_2['APPEARANCES']<=a_mean+(1.5*a_std))]
print(train_3['APPEARANCES'].mean())
# 20.67

# 19번
# 다음은 MASS패키지의 ChickWeight 데이터 세트이다.
# 시간(Time)이 10인 데이터를 훈련 데이터로 생성하고
# 무게(Weight)가 상위 30번째 이상 값을 평균으로 변환한 후
# 변환하기 전, 후의 평균의 차이를 구하시오.
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/Rdatasets/csv/datasets/ChickWeight.csv")
df
df.columns

# 시간(Time)이 10인 데이터를 훈련데이터로 생성하고
tn=df.loc[df['Time']==10]
tn

tn_2=tn.sort_values(by="weight", ascending=False)
tn_2=tn_2.reset_index()
weight_avg=tn_2['weight'].mean()
print(weight_avg)
# 107.8367/3469387755

thirty=tn_2['weight'][29] 
print(thirty)
# 103

tn_2['weight']

print(len(tn.index))
tn=tn.reset_index()
len(tn.index)
# 49

for i in range(0,49):
    if tn['weight'][i]>=thirty:
        tn['weight'][i]=weight_avg
    else:
        pass
after=tn['weight'].mean()

print(weight_avg)
# 107.83
print(after)
# 98.20

print(weight_avg-after)
# 9.6326

# 20번 문제
# 다음은 FIFA Ranking 데이터 세트이다.
# 총점수(total_points)가 상위 3위인 국가(country_abrv)를 선택하고
# 이 국가들 총점수(total_points)항목의 평균을 구하시오.
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/fifa_ranking.csv")
df.columns
df_1=df.sort_values(by="total_points", ascending=False)
df_1=df_1.reset_index()
df_1.drop("index", axis=1, inplace=True)
df_2=df_1.groupby(["country_full", "country_abrv"])['total_points'].sum().reset_index()

df_3=df_2.sort_values(by='total_points', ascending=False)
df_3=df_3.reset_index()
df_3.drop("index", axis=1, inplace=True)
df_3.head(50)
print(df_3.iloc[0, 0], df_3.iloc[1, 0], df_3.iloc[2, 0])
# Germany Argentina Spain

new_df=df.loc[(df["country_full"]=="Germany")|(df["country_full"]=="Argentina")|(df["country_full"]=="Spain")]
new_df=new_df.reset_index()
new_df.drop("index", axis=1, inplace=True)
print(new_df['total_points'].mean())
# 402.21242

# 21번 문제
# 다음은 sales_train 데이터 세트이다. 가장 많이 판매된 상품(item_id) 3가지와 전체 상품에 대하여
# 상품 판매가(item_price) 표준편차 차이를 구하시오.
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/sales_train_v2.csv")
df.columns

# 가장 많이 판매된 상품 3가지
df_2=df.groupby("item_id")['item_cnt_day'].sum().reset_index()
df_3=df_2.sort_values(by="item_cnt_day", ascending=False)
df_3=df_3.reset_index()
df_3.drop("index", axis=1, inplace=True)
df_3.iloc[:3]
# 오답
#  가장 많이 판매된 상품 세 개 item_id: 20949, 2808, 3732
#df_4=df.loc[(df['item_id']==20949)|(df['item_id']==2808)|(df['item_id']==3732)]
#top_3_std=df_4['item_price'].std()
#top_3_std
# 961.067
#all_std=df['item_price'].std()
#all_std
# 1729.799
#print(all_std - top_3_std)
# 768.7317
df.item_id.value_counts()[:3]
df_4=df.loc[(df['item_id']==20949)|(df['item_id']==5822)|(df['item_id']==17717)]
top_3_std=df_4['item_price'].std()
top_3_std
# 628.0034428981169

all_std=df['item_price'].std()
all_std
print(all_std - top_3_std)
#1101.796





