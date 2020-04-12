##################
#ES2 Project 2
#Step 4
#NAME: Kevin Zhang
#HOURS NEEDED: 10 (5 for pseudocode, 5 for code)
#I worked alone on this part.
#################

import numpy as np
import matplotlib.pyplot as plt
import math

def normalizeData(glucose, hemoglobin, classification):
    #this function takes the glucose, hemoglobin and classification arrays as inputs
    #it normalizes glucose and hemoglobin on a 0-1 scale (using their respective min and max)
    #it returns these new glucose and hemoglobin arrays; classification is unchanged
    glucose_scaled = (glucose - 70) / 420
    hemoglobin_scaled = (hemoglobin - 3.1) / 14.7
    return(glucose_scaled, hemoglobin_scaled, classification)

def openckdfile():
    #this function extracts the original glucose, hemoglobin and classification arrays from the data file
    #after extraction, it calls normalizeData to normalize the glucose and hemoglobin arrays
    #it then returns the normalized glucose and hemoglobin arrays, and classification
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return normalizeData(glucose, hemoglobin, classification)

def calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
    #this function takes four inputs: the glucose and hemoglobin values of the test case, and the glucose and hemoglobin arrays
    #it uses the distance formula to calculate the distance from each point in the arrays to the test case
    #it appends each calculated distance to an array, and returns this array
    distancearray =[]
    for i in range(len(glucose)):
        distance = math.sqrt((glucose[i] - newglucose) ** 2 + (hemoglobin[i] - newhemoglobin) ** 2)
        distancearray = np.append(distancearray, distance)
    return distancearray

def create_centroids(k):
    #this function takes one input, k, and returns an array of k elements, with each element being a random centroid
    #each element is an array of two floats from 0-1, corresponding to a random hemoglobin and glucose value respectively
    centroids = np.random.random((k,2))
    return centroids

def assign(centroids, glucose, hemoglobin):
    #this function takes 3 array inputs: a list of centroid points, glucose, and hemoglobin
    #it initializes an array centroid_distances as glucose (just to set the array length; glucose itself is meaningless here)
    #it then traverses centri=oids using a for loop, and calls calculateDistanceArray to generate an array of distances
    #it then vertically stacks these arrays with centroid_distances. Once the for loop is finished, glucose is deleted from the array
    #finally, it creates an array of the indices of the minimum values in each column
    #this corresponds to the centroid that each observation is closest to; this array is then returned
    centroid_distances = glucose
    for i in centroids:
        distances = calculateDistanceArray(i[0], i[1], glucose, hemoglobin)
        centroid_distances = np.vstack((centroid_distances, distances))
    distances_only = np.delete(centroid_distances, 0, axis = 0)
    assignments = np.argmin(distances_only, axis = 0)
    return assignments

def update(centroids, assignments, glucose, hemoglobin):
    #this function takes four array inputs: a list of centroids, a list of centroids assigned to each point, glucose and hemoglobin
    #it first initializes an array new_centroids with filler values (just to set the array length, similar to assign)
    #for each centroid, it uses boolean array indexing to create arrays of the glucose and hemoglobin arrays assigned to each centroid
    #it then takes the average of these two arrays, and combines them into an array, representing the updated centroid
    #these updated centroids are concatenated to new_centroids, to create an array of new centroids
    #the first row (of filler values) is removed, the contents are converted to floats, and the resulting array is returned
    new_centroids = np.array([['imagine having readable code','cant relate']])
    for i in range(len(centroids)):
        glu_values = glucose[assignments == i]
        glu_average = np.average(glu_values)
        hem_values = hemoglobin[assignments == i]
        hem_average = np.average(hem_values)
        new_centroid = np.array([[glu_average, hem_average]])
        new_centroids = np.concatenate((new_centroids, new_centroid))
    centroids_only = np.delete(new_centroids, 0, axis = 0)
    return centroids_only.astype('float64')
    
def display(centroids, glucose, hemoglobin, iteration): 
    #this function takes four inputs: arrays of the centroids, glucose, and hemoglobin, as well as the iteration number
    #it first prints out centroids, after a line stating the iteration number
    #it initializes two arrays representing the glucose and hemoglobin values at the centroids
    #before using a for loop to traverse the centroids array to extract and append these respective values to the arrays
    #it calls split to turn the centroid array into two arrays of its glucose and hemoglobin values
    #it then plots the observations and centroids on a glucose vs hemoglobin scatterplot, in blue and red respectively
    #iteration is used to create the graph title; this is to differentiate the graphs when displayed
    print('Centroids, iteration ', iteration)
    print (centroids)
    glu_centroids = np.array([])
    hem_centroids = np.array([])
    for i in centroids:
        glu_centroids = np.append(glu_centroids, i[0])
        hem_centroids = np.append(hem_centroids, i[1])
    plt.figure()
    plt.title('Glucose vs. Hemoglobin, iteration ' + iteration)
    plt.plot(hemoglobin,glucose, "b.", label = "observations")
    plt.plot(hem_centroids,glu_centroids, "r.", markersize = 20, label = "centroids")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()

def clusterfinder (k, iterations):
    #this function takes two inputs: the number of centroids, and the maximum number of iterations
    #it calls openckdfile() to create the glucose, hemoglobin and classification(unused) arrays
    #it calls create_centroids to create k random initial centroids, and calls display to graph these centroids
    #it then uses a for loop to iterate k times; during each iteration, it calls assign to assign observations to the centroids 
    #it then calls update to modify the original centroids array based on the assignments, and graphs these new centroids
    #once the exit condition is met (e.g. k iterations are complete), the final centroids are printed and returned
    glucose, hemoglobin, classification = openckdfile()
    centroids = create_centroids(k)
    display(centroids, glucose, hemoglobin, '0')
    for i in range(iterations):
        assignments = assign(centroids, glucose, hemoglobin)
        centroids = update(centroids, assignments, glucose, hemoglobin)
        display(centroids, glucose, hemoglobin, str(i + 1))
    print('Final centroids:')
    print(centroids)
    return centroids