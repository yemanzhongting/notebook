# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/12/12 16:43'
from keras.layers import LSTM,Embedding,SimpleRNN,Dense
from keras.models import Sequential
from keras.preprocessing import sequence
import keras.models
from keras.datasets import imdb

max_features=10000
maxlen=500
batch_size=32

(input_train,y_train),(input_test,y_test)=imdb.load_data(num_words=max_features)
input_train=sequence.pad_sequences(input_train,maxlen=maxlen)
input_test=sequence.pad_sequences(input_test,maxlen=maxlen)

model=Sequential()
model.add(Embedding(10000,32))
model.add(SimpleRNN(32))
model.add(Dense(1,activation='sigmoid'))

model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['acc'])

history=model.fit(input_train,y_train,
                  epochs=10,
                  batch_size=128,
                  validation_split=0.2)

model.summary()

import matplotlib.pyplot as plt

acc=history.history['acc']
val_acc=history.history['val_acc']
loss=history.history['loss']
val_loss=history.history['val_loss']

epochs=range(1,len(acc)+1)

plt.plot(epochs,acc,'bo',label='Training acc')
plt.plot(epochs,val_acc,'b',label='Validation acc')

plt.title('Training and validation accuracy')
plt.legend()

plt.figure()

plt.plot(epochs,loss,'bo',label='Training loss')
plt.plot(epochs,val_loss,'b',label='Validation loss')
plt.title('Training and Validation loss')

plt.legend()

plt.show()
from keras.models import load_model
# 保存模型  from keras.models import load_model
model.save('model_simpleRnn.h5')   # HDF5文件，pip install h5py