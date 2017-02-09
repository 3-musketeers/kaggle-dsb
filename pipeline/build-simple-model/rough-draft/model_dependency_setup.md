# Basic Model Package, GPU Setup Instructions
*goal: setup the entire programming environment to be able to run [this](https://github.com/3-musketeers/kaggle-dsb/blob/master/pipeline/build-simple-model/rough-draft/u_net_segmentation_approach.ipynb) ipython notebook*

What needs to be setup?
*(regardless you will need GPU, and a programming environment on your computer because you probably will not be doing all experimentation on the cloud, so focus on setting up GPU and tensorflow, then worry about/think about the data problem later)*

## General Components 
1. GPU 
   1. CUDA
   2. CUDA Tool kit
   3. cuDNN
2. Tensorflow
3. Keras

## Instructions
1. download community version of visual studio ([here](https://www.visualstudio.com/downloads/))
2. follow all instructions [here](http://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/#verify-installation) to setup the cuda tool kit
   1. make sure you follow [these instructions](http://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/#compiling-examples)
   2. run the `deviceQuery` and `bandwidthTest` programs as stated
   3. add to the main program, `getchar()` before the last exit statement (this will prevent the window from closing)
   4. If everything works then cuda toolkit should be all setup
3. download the cuDNN ([here](https://developer.nvidia.com/rdp/cudnn-download))
   1. ignore their download instructions
   2. make sure you know where your cuda directory is located (you can look at the CUDA_PATH to find out), but it should look like: `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v8.0`
   3. unzip the folder
   4. copy the contents according to these instructions ([reference](http://stackoverflow.com/questions/36248056/how-to-setup-cudnn-with-theano-on-windows-7-64-bit))
4. follow [these instructions](http://www.heatonresearch.com/2017/01/01/tensorflow-windows-gpu.html) to create a anaconda virtual environment dedicated to the competition named: "kaggledsb"
   1. a conda-cheatsheet is [here](https://conda.io/docs/_downloads/conda-cheatsheet.pdf)
5. to get into your new virual environment type into anaconda prompt: `activate kaggledsb`
6. install tensorflow by typing into the anaconda terminal: `pip install tensorflow-gpu`
7. install any other packages
8. note for ipython notebooks you need to open them from the anaconda prompt while you are `activate kaggledsb` and in that specific virtual environment
5. install keras by typing into the anaconda terminal: `pip install keras`

## Other Resources
* http://machinelearningmastery.com/introduction-python-deep-learning-library-keras/
* https://github.com/tensorflow/tensorflow/blob/master/tensorflow/g3doc/get_started/os_setup.md#pip-installation-on-windows
* https://github.com/tensorflow/tensorflow/blob/master/tensorflow/g3doc/get_started/os_setup.md#test-the-tensorflow-installation
* https://github.com/tensorflow/tensorflow/blob/master/tensorflow/g3doc/get_started/os_setup.md#optional-install-cuda-gpus-on-linux
* http://www.heatonresearch.com/2017/01/01/tensorflow-windows-gpu.html
* http://www.pyimagesearch.com/2016/07/04/how-to-install-cuda-toolkit-and-cudnn-for-deep-learning/
