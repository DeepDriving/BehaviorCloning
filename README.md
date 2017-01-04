# BehaviorCloning

Udacity self driving course-BehaviorCloning Project

This project is to use deep neural network to do autonmous driving in the simulated enviroment. The simulator run in two modes:  training mode and autonomous mode. During the training mode, we collect the data such as brake, throttle, speed, steering angle as well as images from the vehicle.  In autonomous mode, live image is fed into the trained model which then generates steering angle.

Training Dataset 

Training dataset was generated first by driving the vehicle in simulated mode around the track for several loops.  However, this set of training data is not enough as I found out that model based on this set didnot learn to recover when the vehicle was wandering off the track.  

Eventually, my training data consists of two laps weaving out the right and recovering, and another lap weaving out to the left and recovering and 4 laps of centerline driving.

An example of the training image:

https://github.com/annieguan/BehaviorCloning/blob/master/center_2016_12_06_04_27_10_409.jpg

The dataset was normalized and then randomly shuffled.  I split into 90/10 for training and validation dataset. 

Model

The model I used is the one described in the NVIDIA’s End to End Learning for Self Driving Cars.  

The model has 3 5X5 convolutional layers, followed by 2 3x3 convolutional layers, and 3 fully connected layers and output layer as described in this paper.

https://github.com/annieguan/BehaviorCloning/blob/master/architecture.png

I addded max pooling with pool size of (2,2) to prevent overfitting. 


I optimized the model using Adam Optimizer with a mean-sqaured-error loss metric.

Training Process

I tried 5 epochs.  The training accuracy was about 56% and validation accuracy was 57% each epcho.  Adding more epochs doesnot improve the accuracy.

Testing Process

drive.py is modified to normalize the images as I did in training phase.
