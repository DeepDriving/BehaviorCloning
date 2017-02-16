# BehaviorCloning

Model Architecture Design,
Architecture Characteristics,
Data Preprocessing and
Model Training (Include hyperparameter tuni

# Udacity self driving course-BehaviorCloning Project

This project is to use deep neural network to do autonmous driving in the simulated enviroment. The simulator run in two modes:  training mode and autonomous mode. 

During the training mode, we collect the data such as brake, throttle, speed, steering angle as well as images from the vehicle.  In autonomous mode, live image is fed into the trained model which then generates steering angle.

By manually driving the vehicle in Training Mode and using the images from the vehicle as features, with the associated steering angles as labels, I was able to develop a Deep Neural Network to control the steering of the vehicle as it drove around the track.

## Model Architecture Design

Training Dataset 

Training dataset was generated first by driving the vehicle in simulated mode around the track for several loops.  However, this set of training data is not enough as I found out that model based on this set didnot learn to recover when the vehicle was wandering off the track.  

Eventually, my training data consists of two laps weaving out the right and recovering, and another two laps weaving out to the left and recovering and 4 laps of centerline driving.

An example of the training image:

https://github.com/annieguan/BehaviorCloning/blob/master/center_2016_12_06_04_27_10_409.jpg

The dataset was normalized and then randomly shuffled.  I split into 90/10 for training and validation dataset. 

Model

The network architecture that I used was inspired by a paper titled [End to End Learning for Self-Driving Cars](http://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf). In that paper, they present the following figure which depicts the architecture that they used to map images to steering commands:

![Network Architecture](./architecture.png)

This model consists of data normalization, followed by 3 5x5 convolutional layers, followed by 2 3x3 convolutional layers, followed by 3 fully connected layers, followed by the output layer. The only modification that I made to this architecture was the addition of a 2-Dimensional max-pooling layer after each convolutional layer to further reduce the number of model parameters and help reduce overfitting.


The model summary has the following:

https://github.com/annieguan/BehaviorCloning/blob/master/model_summary.png


I optimized the model using Adam Optimizer with a mean-sqaured-error loss metric.

Training Process

I tried 5 epochs.  The training accuracy was about 56% and validation accuracy was 57% each epcho.  Adding more epochs doesnot improve the accuracy.

Testing Process

drive.py is modified to normalize the images as I did in training phase.
