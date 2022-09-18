#빅데이터분석기사실기연습20211125
# 아래와 같이 주어진 airquality 데이터 세트에서 Solar.R에 결측값이 있는 행을 제거하고,
# Ozone 항목의 결측값을 중앙값으로 대체한 후
# 중앙값으로 대체하기 이전과 이후의 Ozone의
# 표준편차의 차이를 구하시오.
# git clone https://github.com/vincentarelbundock/Rdatasets.git

import pandas as pd
import numpy as np
import sklearn
import xgboost

air=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/Rdatasets/csv/datasets/airquality.csv")
air.drop("Unnamed: 0", axis=1, inplace=True)

# Solar.R 결측값이 있는 행 제거
air_after=air.copy()

air_after['Solar.R']

for i in range(0,153):
    if air_after['Solar.R'][i]>=-10000000000:
        if air_after['Solar.R'][i]<=100000000:
            pass
    else:
        air_after['Solar.R'][i]="결측치"
        
air_after=air_after.loc[air_after['Solar.R']!="결측치"]
before=air_after['Ozone'].std()
print(before)
# 33.27

# Solar.R 결측값이 있는 행 제거
air_after.dropna(axis=0, inplace=True, subset=['Solar.R'])
air_after
before=air_after['Ozone'].std()
print(before)
# 33.27

# Ozone 항목의 결측값을 중앙값으로 대체한 후
ozone_median=air_after['Ozone'].median()
print(ozone_median)
# 31.0
air_after["Ozone"]=air_after["Ozone"].fillna(ozone_median)
air_after.isna().sum()

# 중앙값으로 대체하기 이전과 이후의 Ozone의
# 표준편차의 차이를 구하시오.
print("before :", before)
# before : 32.2759
after=air_after['Ozone'].std()
print("after :", after)
#after : 29.37039856321203

print("중앙값으로 대체하기 이전과 이후의 Ozone의 표준편차의 차이 :", before-after)
# 3.90557

# 2번 문제
# 다음과 같이 Hitters 데이터 세트가 주어졌을 대, Salary의 이상값의 합을 구하시오.
# 단, 이상값은 중위수에서 IQR의 2배를 초과하는 값으로 한다.
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/Hitters.csv")
df=df.set_index("Unnamed: 0")
df.isna().sum()
df['Salary']

df['Salary'].describe()
df['Salary'].isna().sum()
# 결측치 59개
q1=190
q3=750
IQR=q3-q1
print(IQR)
# 560

df['Salary'].loc[df['Salary']>q3+2*IQR].sum()+df['Salary'].loc[df['Salary']<q1-2*IQR].sum()
# 14740.404

print(q3+2*IQR)
#1870
print(q1-2*IQR)
# -930

df_1=df.copy()
df_1.dropna(axis=0, inplace=True, subset=['Salary'])
df_1['Salary'].describe()
q1=np.percentile(df_1['Salary'], 25)
q3=np.percentile(df_1['Salary'], 75)
print(q1, q3)
# 190, 750
IQR=q3-q1
print(IQR)
# 560
med=df_1['Salary'].median()
# 425
low_outlier=med-(2*IQR)
over_outlier=med+(2*IQR)

df_2=df_1.loc[(df_1['Salary']<low_outlier)|(df_1['Salary']>over_outlier)]
df_2['Salary'].sum()
# 21671.86

# 3번 문제
# 주어진 diamonds의 데이터를 순서대로 80% 데이터를 훈련데이터로 만들어서 price 기준으로 상위 100개의 데이터에 대한
# price의 평균을 구하시오.
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/diamonds.csv")
print(len(df.index))
# 53940
print(len(df.index)*0.8)
# 43152.0

train=df.iloc[:43152, :]
print(len(train.index))
# 43152

train_2=train.sort_values("price", ascending=False)
train_3=train_2.reset_index()
train_4=train_3.iloc[:100, :]
print(len(train_4.index))
# 100
train_4['price']
avg=train_4['price'].mean()
print("상위 100개 데이터에 대한 price의 평균 :", avg)
# 18663.33


# 4번 문제
# 다음은 뉴욕의 공기 오염도를 측정한 airquality데이터 세트이다.
# 데이터의 순서대로 90% 데이터를 훈련 데이터로 추출하고
# Ozone 항목의 결측값을 평균으로 변경한 후
# 변경 전, 후의 중앙값 차이를 구하시오.
air=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/Rdatasets/csv/datasets/airquality.csv")
air.drop("Unnamed: 0", axis=1, inplace=True)
air
print(len(air.index))
# 153
print(len(air.index)*0.9)
# 137.7

air_2=air.iloc[:138, :]
print(len(air_2.index))
# 138
air_2['Ozone'].median()
# 35.0

air_3=air_2.copy()
air_3.isna().sum()
ozone_avg=air_3['Ozone'].mean()
print(ozone_avg)
# 45.0490
air_3['Ozone']=air_3['Ozone'].fillna(ozone_avg)
air_3['Ozone'].median()
# 45.0490

after=air_3['Ozone'].median()
print(after)
# 45.0490
before=air_2['Ozone'].median()
print(before)
# 35.0
before-after
# -10.0490

# 5번 문제 
# 다음은 music 데이터 세트이다.
# tempo 항목의 상위 25%와 하위 25%를 0으로 대체하여 훈련데이터를 생성하고
# tempo 항목의 평균과 표준편차의 합을 구하시오.
df_1=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/data.csv")
df_2=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/data_2genre.csv")
df_1.columns
df_2.columns

df_1.head()
df_2.head()
print(len(df_1.index))
# 1000
print(len(df_2.index))
# 200
print(len(df_1.columns))
# 30
print(len(df_2.columns))
# 30

# tempo 항목의 상위 25%와 하위 25%를 0으로 대체하여 훈련데이터를 생성하고
df_1.describe()
df_a=df_1.copy()
df_a['tempo'].describe()
# 25% 99.384014, 75% 135.999178

under_25=np.percentile(df_a['tempo'], 25)
print(under_25)
# 99.384
top_25=np.percentile(df_a['tempo'], 75)
print(top_25)
# 135.99

print(len(df_a.index))
# 1000

df_a.head()
df_a.columns

df_a.iloc[999, 1]

for i in range(0,999):
    if df_a.iloc[i, 1]>top_25:
        df_a.iloc[i, 1]=0
    elif df_a.iloc[i, 1]<under_25:
        df_a.iloc[i, 1]=0
    else:
        pass

df_1['tempo'].describe()
df_a['tempo'].describe()

# tempo 항목의 평균과 표준편차의 합
tempo_avg=df_a['tempo'].mean()
print(tempo_avg)
# 50.98, 65.84
tempo_std=df_a['tempo'].std()
print(tempo_std)
# 58.19, 58.58

print("tempo 항목의 평균과 표준편차의 합 :", tempo_avg+tempo_std)
# 109.1860 (상위 25%, 하위 25% 값 포함)
# 124.4235 (상위 25%, 하위 25% 값 미포함)

# 6번 문제
# telco-customer-chum 데이터 세트이다. TotalCharges 항목에서
# 이상값을 제외한 평균을 구하시오.
# (이상값은 평균에서 1.5표준편차 이상인 값)
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

num=float(df['TotalCharges'][0])
num
print(len(df.index))
# 7043

new_df=df.loc[df['TotalCharges']!=' ']
new_df=new_df.reset_index()
new_df.drop('index', axis=1, inplace=True)
print(len(new_df.index))

for i in range(0,7032):
    num=float(new_df['TotalCharges'][i])
    new_df['TotalCharges'][i]=num
    i+=1


new_df['TotalCharges'].min()
# 18.8
new_df['TotalCharges'].max()
# 8684.8

# TotalCharges 항목에서 이상값을 제외한 평균을 구하시오.
# 이상값: 평균에서 1.5 표준편차 이상인 값
tc_mean=new_df['TotalCharges'].mean()
print(tc_mean)
# 2283.3004
tc_std=new_df['TotalCharges'].std()
print(tc_std)
# 2266.77

tc_over=tc_mean+(1.5*tc_std)
tc_under=tc_mean-(1.5*tc_std)
print(tc_over, tc_under)
# 5683.457483666587 -1116.8566019828477

n_df=new_df.loc[(new_df['TotalCharges']<tc_over)]
nooutlier_avg=n_df['TotalCharges'].mean()
print(nooutlier_avg)
# 1663.995

#7번 문제
# 다음과 같이 고양이 cats의 데이터 세트가 주어질 경우에 심장의 무게(Hwt)의 이상값의 평균을 구하시오.
# (단, MASS 패키지의 cats 데이터 세트를 사용하고, 이상값은 평균에서 1.5배 표준편차를 벗어나는 값으로 한다.)
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/Rdatasets/csv/MASS/cats.csv")
df.drop("Unnamed: 0", axis=1, inplace=True)
df.isna().sum()
hwt_std=df['Hwt'].std()
hwt_mean=df['Hwt'].mean()

over_outlier=hwt_mean+(1.5*hwt_std)
under_outlier=hwt_mean-(1.5*hwt_std)

print(over_outlier, under_outlier)
# 14.2825, 6.978601

over=df.loc[df['Hwt']>over_outlier]
over
under=df.loc[df['Hwt']<under_outlier]
under


over=over.reset_index()
over.drop('index', axis=1, inplace=True)
under=under.reset_index()
under.drop('index', axis=1, inplace=True)

outlier=pd.concat([over, under], axis=0)
outlier
outlier=outlier.reset_index()
outlier.drop('index', axis=1, inplace=True)

print("이상값의 평균", outlier['Hwt'].mean())

#8번 문제
# 다음은 23회의 우주 왕복 임무에서 수집된 데이터이다.
# damage가 1 이상일 경우의 temp와 damage의 피어슨 상관계수를 구하시오.
# 데이터를 찾을 수 없으므로, 9번 문제랑 같이

# 9번 문제
# 주어진 데이터 세트는 32개 자동차 모델의 디자인과 성능을 비교한 mtcars 내장 데이터 세트이다.
# 수동(am=1) 중에서 가장 무게(wt)가 작게 나가는 10개 데이터의 평균 연비(mpg)와 자동(am=0)중에서
# 가장 무게(wt)가 작게 나가는 10개 데이터의 평균 연비(mpg)의 차이를 구하시오.

df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/mtcars.csv")
df.columns
df.corr()

# 8번 문제 응용
# am=1일 경우, hp와 mpg의 피어슨 상관계수를 구하시오.
df_1=df.loc[df['am']==1]
df_1

from scipy import stats
pearson=stats.pearsonr(df_1['hp'], df_1['mpg'])[0]
print("피어슨 상관계수 :", pearson)
spearman=stats.spearmanr(df_1['hp'], df_1['mpg'])[0]
print("스피어만 상관계수 :", spearman)

# 수동(am=1) 중에서 가장 무게(wt)가 작게 나가는 10개 데이터의 평균 연비(mpg)와 자동(am=0)중에서
# 가장 무게(wt)가 작게 나가는 10개 데이터의 평균 연비(mpg)의 차이를 구하시오.
df_1=df.loc[df['am']==1]
df_2=df_1.sort_values('wt', ascending=True)
df_2=df_2.reset_index()
df_2.drop('index', axis=1, inplace=True)
df_2=df_2.iloc[:10, :]
mpg_1=df_2['mpg'].mean()
print("가장 무게가 작게 나가는 10개 데이터의 평균 연비 :", mpg_1)
# 26.52999

df_3=df.loc[df['am']==0]
df_4=df_3.sort_values('wt', ascending=True)
df_4=df_4.reset_index()
df_4.drop('index', axis=1, inplace=True)
df_4=df_4.iloc[:10, :]
mpg_0=df_4['mpg'].mean()
print("가장 무게가 작게 나가는 10개 데이터의 평균 연비 :", mpg_0)
# 19.46

("수동(am=1) 중에서 가장 무게(wt)가 작게 나가는 10개 데이터의 평균 연비(mpg)와 자동(am=0)중에서 가장 무게(wt)가 작게 나가는 10개 데이터의 평균 연비(mpg)의 차이 : ", mpg_1-mpg_0)
# 7.06999

# 10번 문제
# 주어진 diamonds의 데이터를 순서대로 80% 데이터를 제거한 후 cut이 "Fair"이면서 
# carat이 1이상인 diamonds의 price의 최댓값을 구하시오.
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/diamonds.csv")
print(len(df.index))
# 53940
print(len(df.index)*0.8)
# 43152
print(len(df.index)*0.2)
# 10788
df_1=df.iloc[-10788:, :]
print(len(df_1.index))
# 10788
df_2=df_1.loc[(df_1['cut']=="Fair")&(df_1['carat']>1)]
df_1.columns
df_1.cut.unique()

price_max=df_2['price'].max()
print("price의 최댓값 :", price_max)
# price의 최대값: 2745

# 11번 문제
# 다음은 airquality 데이터 세트이다. 8월 21일의 Ozone 값을 구하시오.
air=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/Rdatasets/csv/datasets/airquality.csv")
air_8=air.loc[air['Month']==8]
air_821=air_8.loc[air_8['Day']==21]
air_821_Ozone=air_821['Ozone']
print("8월 21일의 Ozone 값", air_821_Ozone)
# 21.0

air_820=air.loc[(air['Month']==8)&(air['Day']==20)]
air_820['Ozone']
# 44.0

# 12번 문제
# 다음은 iris 데이터 세트이다. Sepal.Length의 mean값과 
# Sepal.Width의 mean 값의 합계를 구하시오.
data=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/Rdatasets/csv/datasets/iris.csv")
data.columns

len_mean=data['Sepal.Length'].mean()
wid_mean=data['Sepal.Width'].mean()
total=len_mean+wid_mean
print("합계 :", total)
# 8.90

# 13번 answp
# 다음은 mtcars 데이터 세트이다. 4기통인 자동차의 백분율(%)을 구하시오.
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/mtcars.csv")
df_4=df.loc[df['cyl']==4]
df_4=df_4.reset_index()
len_df=len(df.index)
len_df4=len(df_4.index)
print("4기통인 자동차의 백분율(%) :", (len_df4/len_df)*100, "%")
# 34.3755

# 14번 문제
# 다음은 mtcars 데이터 세트이다. 변속 기어 수가 4이고 수동 변속기인 데이터에서
# 자동차 연비의 mean값과 전체 마력의 표준편차의 합계를 구하시오.
df_2=df.loc[(df['gear']==4)&(df['am']==1)]
mpg_mean=df_2['mpg'].mean()
hp_std=df_2['hp'].std()

print("합계 :", mpg_mean+hp_std )
# 50.4495

# 15번 문제
# 다음은 BostonHousing 데이터 세트이다.
# crim 항목이 1보다 작거나 같은 경우에 medv 항목의 mean값을 구하시오.
# medv 항목이 없으므로, DIS로 대체
from sklearn import datasets
df=datasets.load_boston()
df.keys()

bos = pd.DataFrame(df.data, columns = df.feature_names)
bos['PRICE']=df.target
bos.columns

bos_2=bos.loc[bos['CRIM']<=1]
dis_mean=bos_2['DIS'].mean()
print("dis 항목의 mean :", dis_mean)

###### 끝 ######