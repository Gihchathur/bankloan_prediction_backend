from sklearn.preprocessing import MinMaxScaler
import numpy as np

print('Hello, world!')
ar = [[12000, 60, 19.69, 315.87, 63996.00, 20.81, 1999,  6.00, 0, 22226.00, 99.20, 38.00, 1.00, 0.00, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] , 
     [40000, 60, 30.99, 1533.81, 600.00, 0.00, 1944.00,  1.00, 0.00, 0.00, 0.00, 2.00, 0.00, 0.00, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0] ,
     [500, 36, 5.32, 16.08, 7446395.00, 1622.00, 2013.00,  90.00, 1.00, 1298783.00, 123.20, 151.00, 1.00, 1.00, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]


print(len(ar[0]))

scaler = MinMaxScaler()
X_test = scaler.fit_transform(ar)

print(X_test[0])
