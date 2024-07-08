# -*- coding: utf-8 -*-
"""Week 3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X7ImtLah8yga5ehF3Mbz9ERPf9l42f12
"""

#Input layer, hidden layer (can have more than one), and output layer
#No SUMmation --> Feed Forward Neural Network
# impoet packages
from tensorflow import keras
from keras.models import Sequential
from keras import Input
from keras.layers import Dense

# data manipulation
import pandas as pd
import numpy as np

# for using the model
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

file_name = "/weatherAUS.csv"

#read in data
df = pd.read_csv(file_name, encoding='utf-8')

pd.options.display.max_columns = 50
df

# clean
print("Missing entries in MinTemp " + str(df['MinTemp'].isnull().sum()))

df = df[pd.isnull(df['RainTomorrow'])==False]

# Fill empty spaces with the mean of the colummn
df = df.fillna(df.mean())

#create the flag for RainToday, RainTomorrow (numerical value corresponding to a non-numerical value)
df['RainTodayFlag'] = df['RainToday'].apply(lambda x: 1 if x=='Yes' else 0)
df['RainTomorrowFlag']=df['RainTomorrow'].apply(lambda x: 1 if x== "Yes" else 0)

#set up and test training stes
X = df[['Humidity3pm']]
y = df['RainTomorrowFlag'].values

#get training and testing samples
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#set up the model structure
model = Sequential(name = "Model-with-One-Input")

#set up the input layer
model.add(Input(shape=(1,), name = 'Input-Layer'))

#create 2 nodes in hidden layers
model.add(Dense(2, activation= 'softplus', name = 'Hidden-Layer')) #softplux(x) = log(exp(x) +1)
#create oupt layer
model.add(Dense(1, activation='sigmoid', name = 'Output-Layer'))

model.compile(loss='binary_crossentropy',
              metrics = ['Accuracy', 'Precision', 'Recall'])

from keras.engine.training import Model
#X_train, y_train
model.fit(X_train,
          y_train,
          batch_size =10,
          epochs=3
          )

#predict labels on our training data
pred_labels_tr = (model.predict(X_train) > 0.5).astype(int)

#predict labels on testing data
pred_labels_te =(model.predict(X_test) >0.5).astype(int)

model.summary()

print(classification_report(y_train, pred_labels_tr))

print(classification_report(y_test, pred_labels_te))