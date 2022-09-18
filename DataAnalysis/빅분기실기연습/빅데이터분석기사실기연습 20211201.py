# 빅데이터분석기사실기연습 20211201
import pandas as pd
import numpy as np
import sklearn 
import scipy
import xgboost

# 2번 문제
# 다음과 같이 Hitters 데이터 세트가 주어졌을 때, Salary의 이상값의 합을 구하시오.
# (단, 이상값은 중위수에서 IQR의 2배를 초과하는 값으로 한다.)
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/Hitters.csv")
df=df.set_index("Unnamed: 0")

new_df=df.copy()
new_df.dropna(axis=0, inplace=True, subset=["Salary"])

q3=np.percentile(new_df['Salary'], 75)
q1=np.percentile(new_df['Salary'], 25)
IQR=q3-q1
sal_med=df['Salary'].median()
over_outlier=sal_med+(2*IQR)

outlier=df.loc[df['Salary']>over_outlier]
print(outlier['Salary'].sum())
# 21671.864

# 4번 문제
# 다음은 뉴욕의 공기 오염도를 측정한 airquality데이터 세트이다.
# 데이터의 순서대로 90% 데이터를 훈련 데이터로 추출하고
# Ozone 항목의 결측값을 평균으로 변경한 후
# 변경 전, 후의 중앙값 차이를 구하시오.
air=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/Rdatasets/csv/datasets/airquality.csv")
air.drop("Unnamed: 0", axis=1, inplace=True)
air

ninety=int(len(air.index)*0.9)
train=air.iloc[:ninety, :]
ozone_mean=train['Ozone'].mean()
new_train=train.copy()
new_train['Ozone']=new_train['Ozone'].fillna(ozone_mean)
print(np.abs(train['Ozone'].median()-new_train['Ozone'].median()))
# 10.363366

# 10번
# 주어진 diamonds의 데이터를 순서대로 80% 데이터를 제거한후 cut이 "Fair"이면서
# carat이 1 이상인 diamonds의 price의 최댓값을 구하시오.
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/diamonds.csv")
df.drop("Unnamed: 0", axis=1, inplace=True)
eighty=int(len(df.index)*0.8)

df_2=df.iloc[eighty:,:]
df_3=df_2.loc[df_2['cut']=="Fair"]
df_4=df_3.loc[df_3['carat']>=1]
print(df_4['price'].max())
# 2745

print(df_2.loc[(df_2['cut']=="Fair")&(df_2['carat']>=1)]["price"].max())
# 2745

# 18번 문제
# 다음은 marvel 데이터 세트이다. Hair가 "Brown Hair"이고
# Eye가 "Brown Eyes"인 데이터를 훈련 데이터로 추출 했을 때, APPEARANCES에서
# 이상값을 제외한 평균을 구하시오.
# (이상값은 평균에서 1.5 표준편차 초과 혹은 미만)
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/dc-wikia-data.csv")
df.columns
df_2=df.loc[(df["HAIR"]=="Brown Hair")&(df['EYE']=="Brown Eyes")]
a_std=df_2["APPEARANCES"].std()
a_mean=df_2["APPEARANCES"].mean()

over_outlier=a_mean+(1.5*a_std)
under_outlier=a_mean-(1.5*a_std)

df_3=df_2.loc[(df_2["APPEARANCES"]<=over_outlier)&(df_2["APPEARANCES"]>=under_outlier)]
print(df_3["APPEARANCES"].mean())
# 20.67105

# 13번. 다음은 mtcars 데이터 세트다. 
# wt 칼럼을 최소 최대 척도(min-max scale)로 변환한 후
# 0.5보다 큰 레코드 수를 구하시오.
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/mtcars.csv")
df=df.set_index('model')

# 1st method
from sklearn.preprocessing import MinMaxScaler
mm=MinMaxScaler()

minmax_wt=mm.fit_transform(df[['wt']])
records=np.where(minmax_wt>0.5)
records=records[0]
print(len(records))
# 11

# 2nd method
len_index=len(df.index)
min_x=df['wt'].min()
max_x=df['wt'].max()

for i in range(len_index):
    x=df['wt'][i]
    z=(x-min_x)/(max_x-min_x)
    df['wt'][i]=z

records=df.loc[df['wt']>0.5]
records=records.reset_index()
print(len(records.index))
# 11

# 다음은 ISLR 패키지의 Carseats 데이터 세트이다.
# 매출(Sales)의 이상값을 제외한 데이터를 훈련 데이터로 선정 할 때
# Age의 표준편차를 구하시오.
# (이상값은 평균보다 1.5 표준편차 이하이거나 이상인 값으로 선정한다.)
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/Rdatasets/csv/ISLR/Carseats.csv")
sales_std=df["Sales"].std()
sales_mean=df['Sales'].mean()

new_df=df.loc[(df['Sales']<sales_mean+(1.5*sales_mean))&(df['Sales']>sales_mean-(1.5*sales_mean))]
print(new_df['Age'].std())
# 16.20
print(sales_std, sales_mean, sales_mean+(1.5*sales_mean), sales_mean-(1.5*sales_mean))

df['Sales'].describe()


# 1번문제
# 아래와 같이 주어진 airquality 데이터 세트에서 Solar.R에 결측값이 있는 행을 제거하고,
# Ozone 항목의 결측값을 중앙값으로 대체한 후
# 중앙값으로 대체하기 이전과 이후의 Ozone의
# 표준편차의 차이를 구하시오.
air=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/Rdatasets/csv/datasets/airquality.csv")
air.drop("Unnamed: 0", axis=1, inplace=True)

air.dropna(axis=0, inplace=True, subset=["Solar.R"])

oz_med=air["Ozone"].median()
before_std=air["Ozone"].std()
air_after=air.copy()
air_after["Ozone"]=air_after["Ozone"].fillna(oz_med)
after_std=air_after["Ozone"].std()
print(np.abs(after_std-before_std))
# 3.90

# 21번 문제
# 다음은 sales_train 데이터 세트이다. 가장 많이 판매된 상품(item_id) 3가지와
# 전체 상품에 대하여
# 상품 판매가(item_price) 표준편차 차이를 구하시오.
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/sales_train_v2.csv")
df.columns

many=df["item_id"].value_counts()
df_many=pd.DataFrame(many)
item_1=df_many.index[0]
item_2=df_many.index[1]
item_3=df_many.index[2]

top_3=df.loc[(df['item_id']==item_1)|(df['item_id']==item_2)|(df['item_id']==item_3)]
top_3_std=top_3['item_price'].std()
all_std=df["item_price"].std()
print(np.abs(all_std-top_3_std))
# 1101.796

##############################################

# 11번 문제
# 다음은 음주, 흡연과 식도암의 관계를 분석하기 위한 환자와
# 대조군의 데이터인 esoph 데이터 세트이다.
# 환자 수(ncases)와 대조군 수(ncontrols)를 합한 새로운 칼럼인
# 관측자 수(nsums)를 생성하고, 음주량과 흡연량에 따른
# 관측자 수(nsums)의 이원 교차표(two-way table)를 생성하여
# 확인하고, 음주량과 흡연량에 따른 관측자 수(nsums)의 카이제곱 값을 구하시오.
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/Rdatasets-master/csv/datasets/esoph.csv")
df["nsums"]=0
len(df.index)

for i in range(len(df.index)):
    x=df["ncases"][i]
    y=df["ncontrols"][i]
    z=x+y
    df["nsums"][i]=z

df.drop("Unnamed: 0", axis=1, inplace=True)
df.columns

df_1=df.groupby(["alcgp","tobgp"])["nsums"].sum().reset_index()
df_2=df_1.pivot(index="alcgp", columns="tobgp", values="nsums")
df_2

import scipy
chi2, pvalue, dof, expected=scipy.stats.chi2_contingency(df_2)
print(chi2)

### t-test, f-test 연습 ###
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/mtcars.csv")

statistics, pvalue=scipy.stats.ttest_rel(df["mpg"], df["disp"])
print(statistics)
print(pvalue)

statistics, pvalue=scipy.stats.f_oneway(df['mpg'],  df['disp'])
print(statistics)
print(pvalue)


### 시간관련 데이터 ##
# datetime 1st method(parse_dates=["칼럼이름"])
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/TimeAge.csv", parse_dates=["date"])
df.info()
#   Column     Non-Null Count  Dtype
#---  ------     --------------  -----
# 0   date       1089 non-null   datetime64[ns]
# 1   time       1089 non-null   int64
# 2   age        1089 non-null   object
# 3   confirmed  1089 non-null   int64
# 4   deceased   1089 non-null   int64

# 2nd method(pandas.to_datetime)
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/TimeAge.csv")
df['date']=pd.to_datetime(df['date'])
df.info()
 #   Column     Non-Null Count  Dtype
#---  ------     --------------  -----
# 0   date       1089 non-null   datetime64[ns]
# 1   time       1089 non-null   int64
# 2   age        1089 non-null   object
# 3   confirmed  1089 non-null   int64
# 4   deceased   1089 non-null   int64

# datetime[ns]에서 str로 변환 후 int로 변환하기
df.date

df['year']=df['date'].dt.year
df['month']=df['date'].dt.month
df['day']=df['date'].dt.day

df['year']=df['year'].astype(int)
df['month']=df['month'].astype(int)
df['day']=df['day'].astype(int)

# 데이터 평가(다진분류)
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/Rdatasets/csv/datasets/iris.csv")
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['Species']=le.fit_transform(df['Species'])
df.drop("Unnamed: 0", axis=1, inplace=True)

from sklearn.model_selection import train_test_split
x=df.drop("Species", axis=1)
y=df["Species"]

x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier, GradientBoostingClassifier
rf=RandomForestClassifier(random_state=42)
ada=AdaBoostClassifier(random_state=42)
gb=GradientBoostingClassifier(random_state=42)

from xgboost import XGBClassifier
xgb=XGBClassifier(random_state=42)

from sklearn.metrics import r2_score

def result(model, x_train, x_test, y_train, y_test):
    model.fit(x_train, y_train)
    train_score=model.score(x_train, y_train)
    pred=model.predict(x_test)
    test_score=model.score(x_test, y_test)
    r2=r2_score(y_test, pred)
    print(train_score, test_score, r2)
    
result(rf, x_train, x_test, y_train, y_test)
# 1.0 1.0 1.0

model=RandomForestClassifier(random_state=42)
model.fit(x_train, y_train)
train_score=model.score(x_train, y_train)
pred=model.predict(x_test)
test_score=model.score(x_test, y_test)
r2=r2_score(y_test, pred)
print(train_score, test_score, r2)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, pred)
#array([[10,  0,  0],
#       [ 0,  9,  0],
#       [ 0,  0, 11]], dtype=int64)

from sklearn.metrics import classification_report
auc_roc=classification_report(y_test, pred)
print(auc_roc)
#              precision    recall  f1-score   support
#
#           0       1.00      1.00      1.00        10      
#           1       1.00      1.00      1.00         9      
#           2       1.00      1.00      1.00        11      
#
#    accuracy                           1.00        30      
#   macro avg       1.00      1.00      1.00        30      
#weighted avg       1.00      1.00      1.00        30  

from sklearn.metrics import multilabel_confusion_matrix
multilabel_confusion_matrix(y_test, pred)
#array([[[20,  0],
#        [ 0, 10]],
#
#       [[21,  0],
#        [ 0,  9]],
#
#       [[19,  0],
#        [ 0, 11]]], dtype=int64)