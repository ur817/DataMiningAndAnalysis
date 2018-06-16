import pandas as pd
import numpy  as np
import csv
from sklearn.svm  import SVC
from sklearn.tree import DecisionTreeClassifier

s=np.arange(10000)
np.random.shuffle(s)
# print(s)
#
# train_df=pd.read_csv('train_data_complete.csv',names=["np1","np2","ap1","ap2"])
# print("****")
# print(train_df.head())
# train_x= pd.DataFrame(train_df.sample(400),columns=["np1","np2","ap1","ap2"])
# print(train_x.head())
# train_x.to_csv('training_data2.csv')
# train_x= pd.DataFrame(train_df.sample(400),columns=["np1","np2","ap1","ap2"])
# print(train_x.head())
# train_x.to_csv('training_data3.csv')
# train_x= pd.DataFrame(train_df.sample(400),columns=["np1","np2","ap1","ap2"])
# print(train_x.head())
# train_x.to_csv('training_data4.csv')
# train_x= pd.DataFrame(train_df.sample(400),columns=["np1","np2","ap1","ap2"])
# print(train_x.head())
# train_x.to_csv('training_data5.csv')
#

to_train_x =pd.read_csv("training_data4.csv")
print(to_train_x.head())

classifier = SVC()
train_data = [to_train_x.np1, to_train_x.np2,to_train_x.ap1,to_train_x.ap2]
train_check =to_train_x.label

print(train_check)
print(train_data)
#
# classifier.fit(train_data,train_check)
# classifier.predict(test_data)