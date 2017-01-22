# Understand Evaluation Metric
*final goal: common sensical/basic understanding of evaluation metric*

## References:
![dsb_eval_metric](https://github.com/the-machine-learners/kaggle-dsb/blob/master/pipeline/understand-context/final-copy/dsb_eval_metric.PNG)
* (from [kaggle-dsb evaluation](https://www.kaggle.com/c/data-science-bowl-2017/details/evaluation))
* "In plain English, this error metric is used where contestants have to predict that something is true or false with a probability (likelihood) ranging from definitely true (1) to equally true (0.5) to definitely false(0)." ([kaggle wiki](https://www.kaggle.com/wiki/LogarithmicLoss))
* "The use of log on the error provides extreme punishments for being both confident and wrong." ([kaggle wiki](https://www.kaggle.com/wiki/LogarithmicLoss))
* Python implementation of code ([kaggle wiki](https://www.kaggle.com/wiki/LogarithmicLoss)):
  
  ```python
  import scipy as sp
  def logloss(act, pred):
    epsilon = 1e-15
    pred = sp.maximum(epsilon, pred)
    pred = sp.minimum(1-epsilon, pred)
    ll = sum(act*sp.log(pred) + sp.subtract(1,act)*sp.log(sp.subtract(1,pred)))
    ll = ll * -1.0/len(act)
    return ll
  ```

## Summary:

**Logarithmic Loss error metric is used when you need to predict that something is true or false with a probability (likelihood) ranging from definitely true (1) to equally true (0.5) to definitely false(0), and there is a higher error for being both confident and wrong.**
