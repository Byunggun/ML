
#cf.DL6-3
import numpy as np
import tensorflow as tf

def read_irsi_softmax():
    iris=np.loadtxt('data\multivariable data/iris_softmax.csv', delimiter=',')
    print(iris.shape) #(150,8)

    #1. train_set/test_set 분리하기 - vstack
    train_set=np.vstack((iris[:40], iris[50:90], iris[100:140]))
    print(train_set)
    print(train_set.shape) #(120, 8)
    test_set=np.vstack((iris[40:50], iris[90:100], iris[140:145]))
    print(test_set)
    print(test_set.shape) #(25, 8)
    return train_set, test_set