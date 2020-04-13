##################
#ES2 Project 2
#NAME: Kevin Zhang
#################

This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).

NearestNeighborClassification.py

NearestNeighborClassification.py contains the functions for Nearest Neighbor and K-Nearest Neighbor classifications (e.g. classifying a test case based on its 1, or k, nearest neighbor observations). 

FUNCTIONS

- normalizeData is a helper function for openckdfile takes three inputs: the glucose, hemoglobin, and classification arrays. It returns these three arrays, with glucose and hemoglobin normalized on a 0 - 1 scale. 
- openckdfile takes no inputs, and extracts the glucose, hemoglobin, and classification files from ckd.csv. It calls normalizeData to normalize glucose and hemoglobin, and returns glucose, hemoglobin, and classification. 
- graphData takes three inputs, the glucose, hemoglobin, and classification arrays. It graphs the observations on a scatterplot of hemoglobin (x) vs glucose (y), with the two different classifications color coded and labeled. 
- createTestCase takes no inputs, and returns a test case in the form of a random glucose value, and a hemoglobin value. 
- calculateDistanceArray takes five inputs: the glucose and hemoglobin values of the test case, and the glucose, hemoglobin, and classification arrays. It returns an array comprising the distances of each observation to the test case. 
- nearestNeighborClassifier takes five inputs: the glucose and hemoglobin values of the test case, and the glucose, hemoglobin and classification arrays. It calls calculateDistanceArray to create an array of distances, finds the index of the minimum distance, and returns the classification of the observation at this index.
- graphTestCase takes five inputs: the glucose and hemoglobin values of the test case, and the glucose, hemoglobin and classification arrays. It graphs the observations and test case on a scatterplot of hemoglobin (x) vs glucose (y), with each classification, and the test case, color coded and labeled.
- kNearestNeighborClassifier takes 6 inputs: k, the glucose and hemoglobin values of the test case, and the glucose, hemoglobin and classification arrays. It calls calculateDistanceArray to create an array of distances, sorts this array from least to greatest, finds the indices of the k smallest distances, and finds the classifications of the observations at these indices, before returning the mode of these classifications.

TO USE

Press run. The file will first create a graph of the original data. It then initiates a for loop with 10 iterations (the exact number can be adjusted); in each iteration, a random test case is created and graphed, and its classifications according to Nearest Neighbor and K-Nearest Neighbor classifications are printed. 

***********************************

KMeansClustering.py

KMeansClustering_Functions.py contains the functions needed to use K-Means clustering on the dataset; e.g. iteratively finding k centroids, and returning these centroids and the accuracy statistics if k=2. It contains no script, however (refer to KMeansClustering_Driver.py).

FUNCTIONS

- normalizeData is a helper function for openckdfile takes three inputs: the glucose, hemoglobin, and classification arrays. It returns these three arrays, with glucose and hemoglobin normalized on a 0 - 1 scale. 
- openckdfile takes no inputs, and extracts the glucose, hemoglobin, and classification files from ckd.csv. It calls normalizeData to normalize glucose and hemoglobin, and returns glucose, hemoglobin, and classification. 
- calculateDistanceArray takes five inputs: the glucose and hemoglobin values of the test case, and the glucose, hemoglobin, and classification arrays. It returns an array comprising the distances of each observation to the test case. 
- create_centroids takes one input, k (the number of centroids), and returns an array of k elements; each element is an array of a random glucose and a random hemoglobin value. 
- assign takes three inputs: an array of centroids, and the glucose and hemoglobin arrays. For each centroid, it calls calculateDistanceArray to create an array of distances; it stacks the distance arrays for each centroid, before finding the indices of the minimum distance in each column. It returns assignments, an array of these indices (with the indices each corresponding to a centroid). 
- split takes one input: an array of centroids, and "splits" it into its glucose and hemoglobin components. It initializes these components as two empty arrays, before traversing centroids and appending the glucose and hemoglobin values of each centroid to their respective array. It returns two arrays, the glucose components and hemoglobin components. 
- colorchooser takes one input: i (a number), and returns a color. The colors chosen are arbitrary (but look nice), and only set for 1<i<3, as these are the expected inputs. 
- update takes five inputs: arrays of centroids, assignments (from assign), glucose, and hemoglobin, as well as an iteration number. It calls split to split centroids into glucose and hemoglobin components, and plots these on a scatterplot. It traverses centroids, using boolean array indexing to select the glucose and hemoglobin values assigned to each centroid, before plotting these values (calling colorchooser to choose a color based on the centroid number). It then takes the average of these glucose and hemoglobin values, and appends them to an array as a new centroid; after all centroids are traversed, this array of new centroids is returned. 
- stats takes two inputs, the assignments and classifications arrays. It swaps the values in assignments if necessary (assuming there are more "CKD" assignments than "No CKD" assignments), and compares the two arrays to count four values: no. observations correctly diagnosed with ckd, no. observations correctly diagnosed without ckd, no. observations incorrectly diagnosed with ckd, and no. observations incorrectly diagnosed without ckd. Using these values, it calculates and prints percentages for true positives, false positives, true negatives, and false negatives, returning nothing. 
-clusterfinder takes two inputs, k (the number of centroids), and the number of iterations. It calls openckdfile to extract glucose, hemoglobin, and classification, before calling create_centroids to create k centroids. It calls assign and update on loop for the given number of iterations (storing the resulting centroids and assignments each time). It then prints the final centroids, and if there are two centroids, calls stats to return the accuracy information of these centroids and clusters. 

TO USE

Don't.

***********************************

KMeansClustering_driver.py

FUNCTIONS

No. 

TO USE

Un-comment one of the three lines at the bottom (each line corresponds to a certain number of centroids: 1, 2, or 3). Press run. The file will plot the k centroids and clusters generated over 8 instances. (8 instances was chosen as past that point, the centroids never significantly change, but it can be changed). The final centroids are returned and printed; furthermore, if there are two clusters, the accuracy stats are also printed. 

