# Luna Mask Extraction
*goal: from the luna dataset, extract the masks for each img, where the mask overlaid on top of the image yields the nodule*

## Files:
* final.py -- contains the final copy code (able to be run with 16GB RAM limitations)
* sandbox.ipynb -- contains the experimentation with the code for final.py
* time_memory_analysis.ipynb -- runs the time_memory_run_file.py to produce line by line information (about time and memory) and also contains final conclusions
* time_memory_run_file.py -- only runs the code for 2 sets of images in the dataset and provides time and memory data
* time_memory_run_file.py.lprof -- contains the data produced by time_memory_analysis.ipynb
* final_run_file.py -- the file to be run over the entire dataset to produce final results

## To Run Final:
1. Open anaconda prompt
2. `activate kaggledsb`
3. `cd` into the directory that `final_run_file.py` is located in 
   * example) `cd C:\Users\kyhan\Desktop\kaggle-dsb\code\pipeline\build-simple-model\luna-mask-extraction`

To run the program with memory restrictions:
```python
python -m memory_profiler --pdb-mmem=X final_run_file.py
```
where X is a number representing the memory threshold in MB ([reference](https://github.com/fabianp/memory_profiler#setting-debugger-breakpoints))
