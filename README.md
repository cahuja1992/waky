# HotWord Detection 

## Data Preparation

### Feature extraction
1. Audio clip has to be divided into several segments by choosing a particular window length.  
2. Then features are to be extracted for each of the audio segment.
3. Extract audio features like 
    1. MFCC, 
    2. delta MFCC, 
    3. Linear Predictive Coding(LPC) coefficients 
    4. Other Frequency domain features like 
        b. Spectral Centroid, 
        c. Spectral Bandwidth, 
        d. Spectral Roll Off  
    5. Temporal domain features like 
        a. Root Mean Square Error (RMSE) 
        b. Zero Crossing Rate. 

### Data Preparation
1. Once the features are extracted, the whole training and test data is divided into training and test dataset. 
2. Feature scaling and normalization of training data is done accross each feature.

## Learning Approaches : Statistical/ML

1. CRF
2. HMM
3. LSTM/GRU 
4. K-Means clustering algorithm with the number of clusters usually much higher than the total number of classes and the cluster centroids are obtained for the normalized training set. 
   1. These cluster centroids form the fingerprint. 


### Python Libraries: 
1. librosa
2. pycrf, hmmlearn, scipy, sklearn

### C++ Libraries:
1. mlpack, dlib
