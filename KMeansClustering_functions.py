##################
#ES2 Project 2
#Step 4
#NAME: Kevin Zhang
#HOURS NEEDED: 12 (5 for pseudocode, 7 for code)
#I worked alone on this part.
#################

import numpy as np
import matplotlib.pyplot as plt
import math
import random as r

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
    #it initializes an array centroid_distances as glucose (just to set the array length)
    #it traverses centroids, calling calculateDistanceArray to make an array of distances
    #it stacks these arrays with centroid_distances; the first row (glucose) is then deleted
    #finally, it creates an array of the indices of the minimum values in each column
    #this corresponds to the centroid that each observation is closest to; this is returned
    centroid_distances = glucose
    for i in centroids:
        distances = calculateDistanceArray(i[0], i[1], glucose, hemoglobin)
        centroid_distances = np.vstack((centroid_distances, distances))
    distances_only = np.delete(centroid_distances, 0, axis = 0)
    assignments = np.argmin(distances_only, axis = 0)
    return assignments

def split(centroids):
    #this function takes an array of centroids as an input
    #it initializes two arrays for glucose and hemoglobin
    #it traverses centroids, and appends glucose and hemoglobin values to the proper arrays
    #it returns these two arrays
    glu_centroids = np.array([])
    hem_centroids = np.array([])
    for i in centroids:
        glu_centroids = np.append(glu_centroids, i[0])
        hem_centroids = np.append(hem_centroids, i[1])
    return (glu_centroids, hem_centroids)

def colorchooser(i):
    #this function takes a number, and returns a color. these colors are arbitrary.
    #only numbers from 0-2 have non-random outputs, corresponding to only 1-3 centroids
    if i == 0:
        return "forestgreen"
    elif i == 1:
        return "skyblue"
    elif i == 2:
        return "salmon"
    else:
        return (r.random(),r.random(),r.random())

def update(centroids, assignments, glucose, hemoglobin, iteration):
    #this function takes five inputs: centroids, assignments, glucose and hemoglobin, and the iteration no.
    #it first initializes an array new_centroids with filler values (to set the array length)
    #it calls split to create two arrays of the glucose and hemoglobin values of the centroids
    #a scatterplot is set up, and these centroids are plotted on it
    #it then traverses centroids; for each centroid, the function uses boolean array indexing 
    #to create glu_values and hem_values: the glucose and hemoglobin values assigned to each centroid
    #these arrays are plotted on the graph, and colorchooser is called to determine their color
    #it then takes the average of glu_values and hem_values, and combines them into an array, 
    #representing the updated centroid; this is concatenated to new_centroids
    #the first (filler) row is removed, and the contents are converted to floats 
    #the resulting array, representing a list of updated centroids, is returned
    new_centroids = np.array([['imagine having readable code','cant relate']])
    glu_centroids, hem_centroids = split(centroids)
    plt.figure()
    plt.title('Glucose vs. Hemoglobin, Iteration ' + iteration)
    plt.plot(hem_centroids,glu_centroids, "r.", markersize = 20, label = "centroids")
    for i in range(len(centroids)):
        glu_values = glucose[assignments == i]
        hem_values = hemoglobin[assignments == i]
        plt.plot(hem_values, glu_values, 'o', markersize = 3, color = colorchooser(i))
        glu_average = np.average(glu_values)
        hem_average = np.average(hem_values)
        new_centroid = np.array([[glu_average, hem_average]])
        new_centroids = np.concatenate((new_centroids, new_centroid))
    centroids_only = np.delete(new_centroids, 0, axis = 0)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    return centroids_only.astype('float64')

def stats(assignments, classification):
    #this function takes two inputs: the final assignments, and classification
    #it assumes that there are more 'no ckd' than 'ckd' assignments, based on the data set
    #in the original data set, a classification of 1 = ckd, and 0 = no ckd
    #if there are more 'ckd' than 'no ckd' assignments, 
    #it is assumed the classification values are swapped (as the points themselves match up)
    #in this case, the function swaps 0 and 1 within assignments
    #it then counts the number of 1s and 0s in classification as actually_ckd and actually_nockd
    #it initializes four counter variables, representing in order,
    #no. observations correctly diagnosed with ckd, no. observations correctly diagnosed without ckd,
    #no. observations incorrectly diagnosed with ckd, and no. observations incorrectly diagnosed without ckd
    #it then calculates and prints the percentages for true/false positives and true/false negatives
    if np.count_nonzero(assignments == 1) > np.count_nonzero(assignments == 0):
        for i in range(len(assignments)):
            if assignments[i] == 0.:
                assignments[i] = 1.
            elif assignments[i] == 1.:
                assignments[i] = 0.
    actually_ckd = np.count_nonzero(classification == 1)
    actually_nockd = np.count_nonzero(classification == 0)
    correct_ckd = 0
    correct_nockd = 0
    misdiagnosed_as_ckd = 0
    misdiagnosed_as_nockd = 0
    for i in range(len(assignments)):
        if assignments[i] == classification[i]:
            if assignments[i] == 1:
                correct_ckd += 1
            else:
                correct_nockd += 1
        else:
            if assignments[i] == 0:
                misdiagnosed_as_nockd += 1
            else:
                misdiagnosed_as_ckd += 1
    print ('True Positives = ' + str(correct_ckd / actually_ckd * 100) + '%')
    print ('False Positives = ' + str(misdiagnosed_as_ckd / actually_nockd * 100) + '%')
    print ('True Negatives = ' + str(correct_nockd / actually_nockd * 100) + '%')
    print ('False Negatives = ' + str(misdiagnosed_as_nockd / actually_ckd * 100) + '%')
    return False
    
def clusterfinder (k, iterations):
    #this function takes two inputs: the no. of centroids, and the maximum no. of iterations
    #it calls openckdfile() to create the glucose, hemoglobin and classification arrays
    #it calls create_centroids to create k random initial centroids
    #it then calls assign to assign observations to the centroids,
    #and calls update to modify the original centroids array based on the assignments.
    #these new centroids are graphed and used as an input for the next iteration.
    #after k iterations are complete, the final centroids are printed and returned
    glucose, hemoglobin, classification = openckdfile()
    assignments = np.array([])
    centroids = create_centroids(k)
    for i in range(iterations + 1):
        assignments = assign(centroids, glucose, hemoglobin)
        centroids = update(centroids, assignments, glucose, hemoglobin, str(i))
    print('Final centroids (glucose, hemoglobin):')
    print(centroids)
    if k == 2:
        stats(assignments, classification)
    return centroids
