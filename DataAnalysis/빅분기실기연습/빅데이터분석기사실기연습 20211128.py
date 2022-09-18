# 빅데이터분석기사실기연습 20211128
# 최종모의고사 1회
# 작업형 제 1유형
# 11. 다음은 Boston Housing 데이터 세트이다.
# 본인 소유의 주택 가격에서 상위 50개의 데이터에 대하여
# 최솟값으로 변환한 후 타운별 1인당 범죄율 값이 1이상인 
# 데이터를 구하시오.
from sklearn import datasets
import pandas as pd
import numpy as np
import sklearn
import scipy
import xgboost

df_1=datasets.load_boston()

df_1.keys()

df=pd.DataFrame(df_1.data, columns=df_1.feature_names)
df['MEDV']=df_1.target

# 본인 소유의 주택 가격에서 상위 50개의 데이터에 대하여
# 최솟값으로 변환한 후 타운별 1인당 범죄율 값이 1이상인 
# 데이터를 구하시오.
new_df=df.sort_values("MEDV", ascending=False)
new_df=new_df.reset_index()
new_df.drop("index", axis=1, inplace=True)
new_df=new_df.iloc[:50, :]
new_df

min_MEDV=new_df['MEDV'].min()
# 34.9

new_df['MEDV']=min_MEDV

print(new_df.loc[new_df['CRIM']>=1]['CRIM'].mean())
# 4.265643

#       CRIM   ZN  INDUS  CHAS    NOX     RM    AGE     DIS   RAD    TAX  PTRATIO       B  LSTAT  MEDV
#2   5.66998  0.0  18.10   1.0  0.631  6.683   96.8  1.3567  24.0  666.0     20.2  375.33   3.73  34.9
#3   6.53876  0.0  18.10   1.0  0.631  7.016   97.5  1.2024  24.0  666.0     20.2  392.05   2.96  34.9
#4   9.23230  0.0  18.10   0.0  0.631  6.216  100.0  1.1691  24.0  666.0     20.2  366.15   9.53  34.9
#5   8.26725  0.0  18.10   1.0  0.668  5.875   89.6  1.1296  24.0  666.0     20.2  347.88   8.88  34.9
#10  2.01019  0.0  19.58   0.0  0.605  7.929   96.2  2.0459   5.0  403.0     14.7  369.30   3.70  34.9
#11  1.51902  0.0  19.58   1.0  0.605  8.375   93.9  2.1620   5.0  403.0     14.7  388.45   3.32  34.9
#13  1.83377  0.0  19.58   1.0  0.605  7.802   98.2  2.0407   5.0  403.0     14.7  389.61   1.92  34.9
#14  1.46336  0.0  19.58   0.0  0.605  7.489   90.8  1.9709   5.0  403.0     14.7  374.43   1.73  34.9
#15  4.89822  0.0  18.10   0.0  0.631  4.970  100.0  1.3325  24.0  666.0     20.2  375.52   3.26  34.9
#30  1.22358  0.0  19.58   0.0  0.605  6.943   97.4  1.8773   5.0  403.0     14.7  363.43   4.59  34.9

# 12. 다음은 iris 데이터 세트이다.
# iris 데이터 세트에서 70% 데이터를 샘플링 후
# 꽃받침 길이의 표준편차를 구하시오.
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/Rdatasets/csv/datasets/iris.csv")
from sklearn.model_selection import train_test_split
train, test=train_test_split(df, test_size=0.3, random_state=42)
train.shape
test.shape
len(df.index)*0.7

print(train['Sepal.Length'].std())
# 0.8333040287887755

# 13번. 다음은 mtcars 데이터 세트다. 
# wt 칼럼을 최소 최대 척도(min-max scale)로 변환한 후
# 0.5보다 큰 레코드 수를 구하시오.
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/mtcars.csv")
df=df.set_index('model')

len(df.index)
# 32

# min-max scaler 공식
# x-min(x)/ max(x)-min(x)
for i in range(0,32):
    max_values=df['wt'].max()
    min_values=df['wt'].min()
    x=df['wt'][i]
    z=(x-min_values)/(max_values-min_values)
    df['wt'][i]=z

print(len(df.loc[df['wt']>0.5].index))
# 27

# 작업형 제 2유형
# 다음은 iris 데이터 세트이다. 주어진 데이터를 이용하여 Species rpart(decision tree), svm 예측 모형을 만든 후,
# 높은 Accuracy 값을 가지는 모델의 예측값을 CSV 파일로 제출하시오.
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/Rdatasets/csv/datasets/iris.csv")
df.columns
# Index(['Unnamed: 0', 'Sepal.Length', 'Sepal.Width', 'Petal.Length',
#       'Petal.Width', 'Species'],

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

df['Species']=le.fit_transform(df['Species'])

x=df.drop(["Unnamed: 0", "Species"], axis=1)
y=df[["Species"]]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.2, random_state=42)

from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier(random_state=42)
dt.fit(x_train, y_train)
dt.score(x_train,y_train)
# 1.0
dt_pred=dt.predict(x_test)

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, pred)
# 0.0

from sklearn import svm
clf=svm.SVC(decision_function_shape="ovo")
clf.fit(x_train, y_train)
clf.score(x_train,y_train)
# 0.975
pred=clf.predict(x_test)

mean_squared_error(y_test, pred)
# 0.0

# decision tree가 학습율이 더 좋으므로, decision tree로 제출
submit=pd.DataFrame(dt_pred, columns=["Species"])

# submit.to_csv("수험번호.csv", index=False)

# 최종 모의고사 2회
# 11번 문제.
# 다음은 ISLR 패키지의 Carseats 데이터 세트이다.
# 매출(Sales)의 이상값을 제외한 데이터를 훈련 데이터로 선정 할 때
# Age의 표준편차를 구하시오.
# (이상값은 평균보다 1.5 표준편차 이하이거나 이상인 값으로 선정한다.)
import pandas as pd
import numpy as np
import sklearn
import xgboost
import scipy
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/Rdatasets/csv/ISLR/Carseats.csv")

sales_mean=df['Sales'].mean()
sales_std=df['Sales'].std()

train=df.loc[(df['Sales']>sales_mean-(1.5*sales_std))&(df['Sales']<sales_mean+(1.5*sales_std))]
print(train['Age'].std())
# 16.05212849

# 12번
# 다음은 MASS 패키지의 Cars93 데이터 세트이다.
# Luggage.room의 결측값을 중앙값으로 변환한 후 변환 전, 후 평균의 차이를 구하시오.
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/Rdatasets/csv/MASS/Cars93.csv")
df.isna().sum()
# Luggage.room 결측치 11개

after_df=df.copy()
df.columns
before_mean=df['Luggage.room'].mean()
# 13.89024

luggage_room_median=df['Luggage.room'].median()
luggage_room_median
# 14

after_df['Luggage.room']=after_df['Luggage.room'].fillna(luggage_room_median)
after_mean=after_df['Luggage.room'].mean()
after_mean
# 13.903225806451612

print(before_mean-after_mean)
# -0.0129819

# 13번 문제
# 다음은 Covid19의 TimeAge 데이터 세트이다. 
# 연령(age)이 20대(20s)인 확진자(confirmed)의 평균과
# 50대(50s)인 확진자(confirmed) 평균의 차이를 구하시오.
# https://www.kaggle.com/kimjihoo/coronavirusdataset?select=TimeAge.csv
df=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/TimeAge.csv")
df

twenty=df.loc[df['age']=="20s"]
fifty=df.loc[df['age']=="50s"]

print(twenty['confirmed'].mean()-fifty['confirmed'].mean())
# 957.0

# 작업형 제 2 유형
# 다음은 고객의 대출 정보인 Loan 데이터 세트이다.
# 전체 데이터를 7:3으로 훈련 데이터, 테스트 데이터로 분할하고,
# 테스트 데이터로 고객의 대출 상환(loan_status)을 예측하고 csv 포맷으로 제출하시오.
data=pd.read_csv("C:/Users/bella/Desktop/SelfStudy/빅데이터분석기사연습/data/Loan payments data.csv")
df=data.copy()
len(df.index)
# 500개

# EDA
df['loan_status'].value_counts()
# 3가지

df.head()
df.isna().sum()
# paid off time 100
# past_due_days 300
df.info()

df.describe()
# past_due_days: float 64

due_mean=df['past_due_days'].mean()
df['past_due_days']=df['past_due_days'].fillna(due_mean)

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['Loan_ID']=le.fit_transform(df['Loan_ID'])
df['loan_status']=le.fit_transform(df['loan_status'])
df['education']=le.fit_transform(df['education'])
df['Gender']=le.fit_transform(df['Gender'])

df.head()
df['loan_status'].value_counts()
# 2 300
# 1 100
# 0 100
data['loan_status'].value_counts()
# PAIDOFF 300
# COLLECTION 100
# COLLECTION_PAIDOFF 100

df.head()
len(df.index)

for i in range(0,500):
    z=df['effective_date'][i].split('/')[0]+df['effective_date'][i].split('/')[1]+df['effective_date'][i].split('/')[2]
    df['effective_date'][i]=z

for i in range(0,500):
    z=df['due_date'][i].split('/')[0]+df['due_date'][i].split('/')[1]+df['due_date'][i].split('/')[2]
    df['due_date'][i]=z

df['paid_off_time_1']=0
df['paid_off_time_2']=0

df['paid_off_time']=df['paid_off_time'].fillna("0/0/0 0:0")

for i in range(0,500):
    y=df['paid_off_time'][i].split()[0]
    z=y.split('/')[0]+y.split('/')[1]+y.split('/')[2]
    df['paid_off_time_1'][i]=z

for i in range(0,500):
    y=df['paid_off_time'][i].split()[1]
    z=y.split(':')[0]+y.split(':')[1]
    df['paid_off_time_2'][i]=z

df.drop("paid_off_time", axis=1, inplace=True)

df["due_date"]=df["due_date"].astype(int)
df["effective_date"]=df["effective_date"].astype(int)

df.info()

# 7:3으로 훈련데이터와 테스트 데이터 분리하기
# 2nd method 랜덤으로 7:3 나누기

# 2nd method
# 순차적으로 7:3으로 나누기
from sklearn.model_selection import train_test_split

x=df.drop("loan_status", axis=1)
y=df["loan_status"]

x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.3, random_state=42)

# modeling
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier

tree=DecisionTreeClassifier(random_state=42)
ada=AdaBoostClassifier(random_state=42)
rf=RandomForestClassifier(random_state=42)
gb=GradientBoostingClassifier(random_state=42)
xgb=XGBClassifier(random_state=42)


from sklearn.metrics import r2_score

def result(model, x_train, x_test, y_train, y_test):
    model.fit(x_train, y_train)
    train_score=model.score(x_train, y_train)
    pred=model.predict(x_test)
    test_score=r2_score(y_test, pred)
    model_score=model.score(x_test, y_test)
    print(train_score, test_score, model_score)
    
result(tree, x_train, x_test, y_train, y_test)
# 1.0 0.989 0.9933
result(ada, x_train, x_test, y_train, y_test)
# 1.0 1.0 1.0
result(rf, x_train, x_test, y_train, y_test)
# 1.0 0.9897 0.9933
result(xgb, x_train, x_test, y_train, y_test)
# 1.0 0.9897 0.9933

ada.fit(x_train, y_train)
train_score=ada.score(x_train, y_train)
pred=ada.predict(x_test)
test_score=r2_score(y_test, pred)
model_score=ada.score(x_test, y_test)

print(train_score, test_score, model_score)

submit=pd.DataFrame(pred, columns=["loan_status"])
submit

# submit.csv("수험번호.csv", index=False)

