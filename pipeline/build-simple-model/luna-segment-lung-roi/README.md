# Luna Segment ROi
*goal: from the images and masks, extract only the lungs*

## Files:
* final.py -- contains the final copy code (able to be run with 16GB RAM limitations)
* sandbox.ipynb -- contains the experimentation with the code for final.py
* final_run_file.py -- the file to be run over the entire dataset to produce final results
* check_correctness.ipynb -- notebook to check that final_run_file.py is working correctly

## To Run Final:
1. Open anaconda prompt
2. `activate kaggledsb`

To run the program with memory restrictions:
```python
python -m memory_profiler --pdb-mmem=X C:\Users\kyhan\Desktop\kaggle-dsb\code\pipeline\build-simple-model\luna-segment-lung-roi\final_run_file.py
```
where X is a number representing the memory threshold in MB ([reference](https://github.com/fabianp/memory_profiler#setting-debugger-breakpoints))