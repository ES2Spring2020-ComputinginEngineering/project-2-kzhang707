##################
#ES2 Project 2
#Step 4
#NAME: Kevin Zhang
#################

#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc 

#returns 2 centroids after 8 iterations; the centroids at each iteration are printed and plotted
#after 8 iterations, the centroids shift by less than 1.0*10^-8 units in each direction, a negligible amount
centroids = kmc.clusterfinder(4, 8)
