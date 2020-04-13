##################
#ES2 Project 2
#Step 4
#NAME: Kevin Zhang
#################

#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc 

#run one line below to return 1,2, or 3 centroids after 8 iterations 
#the centroids and their respective clusters are plotted each time
#after testing, I chose 8 iterations as the exit condition
#as after that, the centroids shift by less than 1.0*10^-8 units, a negligible amount

#centroids = kmc.clusterfinder(1, 8)
#centroids = kmc.clusterfinder(2, 8)
centroids = kmc.clusterfinder(3, 8)
