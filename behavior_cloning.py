from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D
from keras.layers.core import Flatten,Dropout
import matplotlib.image as mpimg
import numpy as np
from sklearn.model_selection import train_test_split
import math
import csv
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt

batch_size = 32 
nb_epochs = 5 


def preprocessing(image):

    image= image.astype('float32')
    image= image/255-0.5

    return image


def load_data():
	with open('driving_log.csv', 'r') as f:
		reader = csv.reader(f)
		data = np.array([row for row in reader])
		#print (data)
	train_list = []
	validatation_list = []
	#split train and validatation data
	np.random.shuffle(data)
	split = int(len(data)*0.9)
	
	train_list = data[:split]
	validatation_list = data[split:]
	return (train_list,validatation_list)


def gen_batches(data_list,batch_size):
	features = []
	labels = []
	size = 0
	while True:

		for data in data_list:
			image = [preprocessing(imread(data[0]))]
			angle = data[3].astype('float32')
			features += image
			labels+=[angle]
			size +=1
			if (size==batch_size):
				yield(np.array(features), np.array(labels))
				size=0
				features = []
				labels= []


train_list,validation_list=load_data()

model = Sequential()

# 1st conv layer--5*5 convolution with 24 filters
model.add(Convolution2D(24,5,5,border_mode='valid', input_shape=(160,320,3)))
model.add(MaxPooling2D((2, 2)))
model.add(Activation('relu'))

# 2nd conv layer --5*5 convlution with 36 filters
model.add(Convolution2D(36,5,5,border_mode='valid'))
model.add(MaxPooling2D((2, 2)))
model.add(Activation('relu'))

# 3rd conv layer --5*5 convlution with 48 filters
model.add(Convolution2D(48,5,5,border_mode='valid'))
model.add(MaxPooling2D((2, 2)))
model.add(Activation('relu'))

# 4th conv layer -- 3*3 convolution with 64 filters
model.add(Convolution2D(64,3,3,border_mode='valid'))
model.add(MaxPooling2D((2,2)))
model.add(Activation('relu'))

# 5th conv layer -- 3*3 convoluaiton with 64 filters
model.add(Convolution2D(64,3,3,border_mode='valid'))
model.add(MaxPooling2D((2,2)))
model.add(Activation('relu'))

model.add(Flatten())
#model.add(Dropout(0.2))

#first fully connected layer
model.add(Dense(100))
model.add(Activation('relu'))

#2nd fully connected layer
model.add(Dense(50))
model.add(Activation('relu'))

model.add(Dense(10))
model.add(Activation('relu'))

model.add(Dense(1))

model.summary()
model.compile(optimizer='adam',loss='mse',metrics=['accuracy'])

train_samples_per_epoch = batch_size * math.floor(len(train_list)/batch_size)
valiation_samples_per_epoch = batch_size * math.floor(len(validation_list)/batch_size)
history = model.fit_generator(gen_batches(train_list,batch_size), len(train_list),nb_epoch=nb_epochs, verbose=1,
   			                  validation_data=gen_batches(validation_list, batch_size), nb_val_samples=len(validation_list))



json = model.to_json()
model.save_weights('model.h5')
with open('model.json', 'w') as f:
	f.write(json)


