# "Bulid Simple Model" Module

**input**: specific kaggle competition information, data

**output**: a simple model that creates an actual submission to the competition

## Process:
1. ([understand-data](https://github.com/the-machine-learners/kaggle-dsb/tree/master/pipeline/build-simple-model/rough-draft/understand-data)) understand the data at a deeper level (EDA, preprocessing steps from others)
2. Do these steps in [sandbox](https://github.com/the-machine-learners/kaggle-dsb/blob/master/pipeline/build-simple-model/rough-draft/mxnet_xgboost_baseline_sandbox.ipynb), and [final](https://github.com/the-machine-learners/kaggle-dsb/blob/master/pipeline/build-simple-model/rough-draft/mxnet_xgboost_baseline_final.ipynb):
   1. Extract the basic features from dataset, and build a basic feature matrix
   2. Train simple model using the basic feature matrix
   3. Use simple model to make predictions for the test set
   4. Create submission formatting function 
   5. ([kaggle-dsb](https://www.kaggle.com/c/data-science-bowl-2017)) Submit to public leaderboard

