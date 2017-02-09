# Basic Model Setup Instructions
*goal: setup the entire environment to be able to run [this](https://github.com/3-musketeers/kaggle-dsb/blob/master/pipeline/build-simple-model/rough-draft/u_net_segmentation_approach.ipynb) ipython notebook*

What needs to be setup?
*(regardless you will need GPU, and a programming environment on your computer because you probably will not be doing all experimentation on the cloud, so focus on setting up GPU and tensorflow, then worry about/think about the data problem later)*

## General Process
1. GPU 
   1. CUDA
   2. CUDA Tool kit
   3. cuDNN
2. Tensorflow
3. Keras
4. Data
   1. competition data
   2. luna16 data

## Pending Process
1. setup visual studio make sure it is working
2. redownload the Cuda tool kit and make sure it works with the visual studio compiler
3. download the cuDNN, and make sure it works
4. download tensorflow and make sure it works
5. download keras and make sure it works

http://machinelearningmastery.com/introduction-python-deep-learning-library-keras/
https://github.com/tensorflow/tensorflow/blob/master/tensorflow/g3doc/get_started/os_setup.md#pip-installation-on-windows
https://github.com/tensorflow/tensorflow/blob/master/tensorflow/g3doc/get_started/os_setup.md#test-the-tensorflow-installation
https://github.com/tensorflow/tensorflow/blob/master/tensorflow/g3doc/get_started/os_setup.md#optional-install-cuda-gpus-on-linux
http://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/#abstract
https://www.visualstudio.com/vs/getting-started/

http://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/#verify-installation
http://www.heatonresearch.com/2017/01/01/tensorflow-windows-gpu.html

C:\ProgramData\NVIDIA Corporation\CUDA Samples\v8.0\1_Utilities\bandwidthTest

## Issues
* What if the data cannot fit on the computer?
  * competition data- experiment with the sample

### Data issue 
(so how are we going to make use of AWS, and what is the workflow going to look like? are you going to download all the data to your computer? is it worth it? or do you just need sample datasets? and you run the stuff for all of the dataset on the cloud?)

#### 1 option
1. Use sample datasets to make the code, and make sure it works for all of the data
2. port the code over to AWS, where the entire dataset is stored and run the code for the entire dataset

#### Questions
1. is it fast enough to run the model on the laptop alone? (so you don't need instances?)
2. can you really just use a sample dataset to make all the code, or do you need to be experimenting with all the code?
