# Basic Model Data Setup Instructions
*what data to download to be able to start experimenting and running the code


Now that all the dependencies are setup
just need to download the data to be able to start experimenting
the best thing would be able to download all the data so you can experiment freely, no need to worry about storage and the like
  but if you don't need all the data to be able to work with code

is all the code run on the server going to be code that we have verified will work, and just needs to be run to fulfill a purpose (or are we also going to have the server for experimentation purposes such as testing to see if code will work)

Questions to be answered:
1. Is the code run on the server only going to be working code (that we know will suceed and we just need computation power)? Or will the code run on the server be working code as well as experimentation, so where we can determine what code works and does not work? **Basically what code should be run on the server?**
2. Is it enough just to be experimenting with a sample of the dataset?
3. Can you download sample sets of the data?
   1. Yes, for both Luna16 as well as kaggle competition

We need storage on EBS, so the question is, could we just store our files on my harddrive and dropbox

i can experiment with stuff already because i know i can download a subset of the luna data

1. wait till we get the 4TB harddrive, then download all the data to the harddrive (it really doesn't cost you much to do it as you most likely won't fill up all 4TB, and you can do it overnight, so you might as well because it could benefit your experimentation in the future
2. for now, download subset of data, and start coding and experimenting with the subset of the data and make the code work (once the code works, start learning other stuff and get the other stuff to work as well)
3. on the cloud, download all the data, setup all the environments
   1. This way when you need heavy computation on the entire dataset, you can do it in the cloud instead of doing it locally
   2. the cloud's purpose: heavy computation on the entire dataset (that cannot be done in a reasonable amount of time on the computer's computation power)
   3. if it can be done on the computer in a reasonable amount of time, then do it on the computer (use the cloud as sparingly as possible because you will never know when you might need it in the future
   4. that is why you need to have all the data downloaded to the harddrive, this way you can experiment with the entire dataset straight from your computer (consider getting a bigger harddrive with faster read, write speeds then)
4. don't setup the cloud until you need heavy computation that you cannot do straight from your computer

1. If you have 4TB harddrive, then download all the data to the harddrive
2. If you need heavy computation that cannot be done on the computer:
   1. Setup EBS with all the data
   2. Setup a AWS EC2 instance 
   3. Run the code in the cloud
3. Otherwise:
   1. Download sample sets of the data (until you can get all the data, at which point you can start experimenting with the entire dataset)
   2. Understand the data
   3. Understand the code, by implementing it on the sample set of data
   4. Make sure the code works if it was to be extended to the entire set of data
   5. Setup a final notebook to run over the entire dataset, create a model and generate predictions
   6. When you have all the data downloaded to your computer:
      1. run the successful code over the entire set of data
      2. generate predictions and submit
   7. Loop over this continuosly
      1. Learning other stuff (machine learning, domain specific knowledge to apply to the model)
      2. Implementing it in code
      3. Experiment and see if it works
      4. If it doesn't work scrap it, otherwise keep it and keep improving

https://luna16.grand-challenge.org/download/
http://academictorrents.com/collection/luna-lung-nodule-analysis-16---isbi-2016-challenge

download all data to computer 
or
download sample set of data to computer

Types of Data
   1. competition data
   2. luna16 data


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
