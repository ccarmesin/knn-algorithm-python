from __future__ import division, print_function, unicode_literals

import plot
import clothingDataset
import numpy as np
import os
from operator import itemgetter

# Root path of the project
ROOT_DIR = os.path.abspath(os.curdir)

def knn(trainSet, testPoint, nearestNeighbors=3):

    for trainPoint in trainSet:

        # Measure the distance between the points on x and y axis
        deltaX = trainPoint.get("x") - testPoint.get("x")
        deltaY = trainPoint.get("y") - testPoint.get("y")

        # Apply a² - b² = c² to get the distance to each trainPoint
        distance = np.sqrt(deltaX * deltaX + deltaY * deltaY)
        trainPoint.update({"distance": distance})

    # Take the lowest n distances
    sortedList = sorted(trainSet, key=itemgetter("distance"))[:nearestNeighbors]

    # Predict class of the just calculated distances
    prediction = classifyPoint(sortedList)

    print(prediction)
    return prediction

def classifyPoint(closestPoints):


    closestPointsLen = len(closestPoints)
    labels = {}
    highestLabel = {"number": 0}

    # Count all labels in labels object
    for datapoint in closestPoints:

        label = datapoint.get("label")
        if labels.get(label) is None:
            value = 1
        else:
            value = labels.get(label) + 1

        labels.update({label: value})


    # Search for the highest label
    for label in labels:

        # If current is higher than highestLabel overwrite it!
        if labels.get(label) > highestLabel.get("number"):
            highestLabel = {
                "number": labels.get(label),
                "label": label,
                "probability": (labels.get(label) / closestPointsLen) * 100}

    return highestLabel

if __name__ == "__main__":

    config = {
        "total": 400,
        "trainTestRatio": 4/5,
        "file": ROOT_DIR + "/sizes.xlsx"
    }

    trainSet, testSet = clothingDataset.loadClothingSizeDataset(config)
    print("Train set:", len(trainSet))
    print("Test set:", len(testSet))

    testPoint = testSet[0]
    knn(trainSet, testPoint, 5)

    plot.drawFigure(trainSet, testPoint)