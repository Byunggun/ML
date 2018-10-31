#
import numpy as np
import tensorflow as tf

def read_irsi_softmax():
    iris=np.loadtxt('D:\Python\DlgsPark\data\multivariable data/iris_softmax.csv', delimiter=',')
    print(iris.shape) #(150,8)

    #1. train_set/test_set 분리하기
    #방법1) vstack
    train_set=np.vstack((iris[:40], iris[50:90], iris[100:140]))
    print(train_set)
    print(train_set.shape) #(120, 8)
    test_set=np.vstack((iris[40:50], iris[90:100], iris[140:145]))
    print(test_set)
    print(test_set.shape) #(25, 8)
    return train_set, test_set

    #방법2) 이렇게 작성하면 안됨. 각 위치 요소끼리 합
    # train_set=iris[:40]+iris[50:90]+iris[100:140] #이렇게 작성하면 40행까지의 값+50~90행의 값+100~140행의 값이 더해짐.
    # print(train_set)
    # print(train_set.shape) #(40, 8)


train_set, test_set=read_irsi_softmax()
