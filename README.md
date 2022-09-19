Comparing NumPy vs Eigen (C++)
==============================
The current (comparable) code version in Numpy and Eigen (native) show that
the Eigen implementation is upto 3X faster. We are of course talking
sub-millisecond timescales for a 4x3 matrix. However, I'm guessing this
relative speed-up means larger gains for bigger matrices (e.g. 90x3), where
instead of 0.6 s we now have 0.2s  - which could mean a lot more 
computations over a unit time. 

Broad results
-------------
Essentially the C++ (Eigen) implementation is >= 4 times faster than the 
Python (NumPy) based implementation for a simple 4-channel mic array. Times
for 4 runs reported in nanoseconds.

| NumPy | Eigen | Speedup |
|-------|-------|---------|
|185753 | 43919 |   4.23  |
|187291 | 43342 |   4.32  |
|197276 | 42374 |   4.65  |

Speedups from function implementations
--------------------------------------
Here are the results for 1000 runs with 4-19 channels, and randomly chosen
positions and time-differences of arrival. 

The code has been run in Python using ```cppyy``` linked with Eigen and 
my own C++ implementation. 

| Min-Max  | 95%ile  | Median |
|----------|---------|--------|
| 2.47-7.29|2.68-3.65|  2.99  |
 
In general - we see an overall speedup, with some very promising speedups! The slight decrease
in speedup might be because of the data-marshalling required by switching between languages
(deliberately assigning values of arrays between NumPy and Eigen). 

Data marshalling reduces effective speedups!
--------------------------------------------
Once we factor in the time taken to convert between NumPy arrays and Eigen MatrixXd's - the
effective speedups drop a bit. (For 10,000 runs with randomly chosen number of mics, positions and TDOAs.

| Min-Max    | 95%ile  | Median |
|------------|---------|--------|
| 0.0003-7.14|2.18-2.88|  2.47  |

I can't quite explain the drastic slow-down in some cases. However, I can say that only 
3 of the 10,000 runs showed speed-up factors < 1. 


