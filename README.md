# BehaviorCloning
Udacity self driving course-BehaviorCloning Project

This project is to use deep neural network to do autonmous driving in the simulated enviroment. The simulator run in two modes:  training mode and autonomous mode. During the training mode, we collect the data such as brake, throttle, speed, steering angle as well as images from the vehicle.  In autonomous mode, live image is fed into the trained model which then generates steering angle.

Training Dataset 

Training dataset was generated first by driving the vehicle in simulated mode around the track for several loops.  However, this set of training data is not enough as I found out that model based on this set didnot learn to recover when the vehicle was wandering off the track.  

Eventually, my training data consists of two laps weaving out the right and recovering, and another lap weaving out to the left and recovering and 4 laps of centerline driving.

The dataset was randomly shuffled and then split into 90/10 for training and validation dataset. 

Model

The model I used is the one described in the NVIDIA’s End to End Learning for Self Driving Cars.  

The model has 3 5X5 convolutional layers, followed by 2 3x3 convolutional layers, and  3 fully connected layers and output layer.


____________________________________________________________________________________________________
Layer (type)                     Output Shape          Param #     Connected to                     
====================================================================================================
convolution2d_1 (Convolution2D)  (None, 156, 316, 24)  1824        convolution2d_input_1[0][0]      
____________________________________________________________________________________________________
maxpooling2d_1 (MaxPooling2D)    (None, 156, 158, 12)  0           convolution2d_1[0][0]            
____________________________________________________________________________________________________
activation_1 (Activation)        (None, 156, 158, 12)  0           maxpooling2d_1[0][0]             
____________________________________________________________________________________________________
convolution2d_2 (Convolution2D)  (None, 152, 154, 36)  10836       activation_1[0][0]               
____________________________________________________________________________________________________
maxpooling2d_2 (MaxPooling2D)    (None, 76, 77, 36)    0           convolution2d_2[0][0]            
____________________________________________________________________________________________________
activation_2 (Activation)        (None, 76, 77, 36)    0           maxpooling2d_2[0][0]             
____________________________________________________________________________________________________
convolution2d_3 (Convolution2D)  (None, 72, 73, 48)    43248       activation_2[0][0]               
____________________________________________________________________________________________________
maxpooling2d_3 (MaxPooling2D)    (None, 36, 36, 48)    0           convolution2d_3[0][0]            
____________________________________________________________________________________________________
activation_3 (Activation)        (None, 36, 36, 48)    0           maxpooling2d_3[0][0]             
____________________________________________________________________________________________________
convolution2d_4 (Convolution2D)  (None, 34, 34, 64)    27712       activation_3[0][0]               
____________________________________________________________________________________________________
maxpooling2d_4 (MaxPooling2D)    (None, 17, 17, 64)    0           convolution2d_4[0][0]            
____________________________________________________________________________________________________
activation_4 (Activation)        (None, 17, 17, 64)    0           maxpooling2d_4[0][0]             
____________________________________________________________________________________________________
convolution2d_5 (Convolution2D)  (None, 15, 15, 64)    36928       activation_4[0][0]               
____________________________________________________________________________________________________
maxpooling2d_5 (MaxPooling2D)    (None, 7, 7, 64)      0           convolution2d_5[0][0]            
____________________________________________________________________________________________________
activation_5 (Activation)        (None, 7, 7, 64)      0           maxpooling2d_5[0][0]             
____________________________________________________________________________________________________
flatten_1 (Flatten)              (None, 3136)          0           activation_5[0][0]               
____________________________________________________________________________________________________
dense_1 (Dense)                  (None, 100)           313700      flatten_1[0][0]                  
____________________________________________________________________________________________________
activation_6 (Activation)        (None, 100)           0           dense_1[0][0]                    
____________________________________________________________________________________________________
dense_2 (Dense)                  (None, 50)            5050        activation_6[0][0]               
____________________________________________________________________________________________________
activation_7 (Activation)        (None, 50)            0           dense_2[0][0]                    
____________________________________________________________________________________________________
dense_3 (Dense)                  (None, 10)            510         activation_7[0][0]               
____________________________________________________________________________________________________
activation_8 (Activation)        (None, 10)            0           dense_3[0][0]                    
____________________________________________________________________________________________________
dense_4 (Dense)                  (None, 1)             11          activation_8[0][0]               
====================================================================================================

I optimized the 
Training Process
I tried 5 epochs.  The training accuracy is about 56% and validation accuracy is 57%%
