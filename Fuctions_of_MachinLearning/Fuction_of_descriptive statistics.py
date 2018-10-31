#descriptive statistics&split&np.arg&stack

############################### 연속형 변수 -> 기술통계량(descriptive statistics) 집계 함수 ######################################################

# 그룹화    ->  그룹    ->   요약
# 딕셔너리
# 시리즈
# 함수

import pandas as pd
import numpy as np
from pandas import DataFrame,Series

df=DataFrame({'group':['a','a','a','b','b','b'],
              'value_1':np.arange(6),
              'value_2':np.random.randn(6)})
# print(df)

#1) 그룹화 하기 : df.groupby('')
grouped=df.groupby('group')
# print(grouped) #그룹화는 포장된 채로 나온다, 즉 포장지만 나오게 된다. 단지 어디에 저장되어 있다라는 간략한 내용만 포함된다.

# print(grouped.count()) #그룹 내의 non_NA 개수(NaN 제외한 개수)
# print(grouped.sum()) #그룹 내의 non_NA 합

# print(type(grouped.sum())) #=>DataFrame
# print(grouped.sum()['value_2'])
# print(grouped['value_2'].sum()) #{내 문장}
# print(type(grouped.sum()['value_2'])) #=>Series

df2=DataFrame(grouped.sum()['value_2']) #DataFrame -> Series
# print(df2)
# print(type(df2)) #=>DataFrame

print("="*50)

#2)기술통계량
#[편리함]내장함수
# print(df)
print("최소 : \n",grouped.min())#최소
# print("최대 : \n",grouped.max())#최대
# print("평균 : \n",grouped.mean())#평균
# print("중앙값 : \n",grouped.median()) # 중앙값
# print("표준편차 : \n",grouped.std()) # 표준편차
# print("분산 : \n",grouped.var()) #분산
print("분위수 : \n",grouped.quantile(0.1)) #분위수(0~1사이의 값)
# #각 그룹별 최소값~최대값에 대해 지정된 위치값을 추출
# #a:0~2, b:3~5 0.1 = 10% 위치
 print("그룹내 첫번째 값 : \n",grouped.first()) #그룹내 첫번째 값
# print("그룹내 마지막 값 : \n",grouped.last()) #그룹내 마지막 값
#
 print("그룹별 기술통계량 : \n",grouped.describe()['value_1']) #[중요]describe()[]
# print("그룹별 기술통계량 : \n",grouped.describe()['value_1'].T) #세로로 보기

#[불편함] 사용자 정의 함수 만들어
def iqr_func(x):
    q3,q1=np.percentile(x,[75,25]) #75~25%
    iqr=q3-q1
    return iqr

 print(grouped.aggregate(iqr_func)) #aggregate(내가 정의한 함수) : 내가 집계한 함수 사용하기
 print(grouped.agg(iqr_func)) #위와 동일
 print(grouped.quantile([0.75,0.25]))
#=>해석
# 1.5-0.5 =1
# 4.5-3.5=1
# 1.296474-(-0.30)=1.6
