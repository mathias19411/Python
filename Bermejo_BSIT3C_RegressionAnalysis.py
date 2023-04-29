import math
from pandas import *

def regressionAnalysis(xList, yList, xNewList):

    xAverage = sum(xList) / len(xList) #x variable average
    xAverage = math.ceil(xAverage * 100) / 100 
    yAverage = sum(yList) / len(yList) #y variable average
    yAverage = math.ceil(yAverage * 100) / 100
    print("The Average of X: ", xAverage) #10 - 1 dec place, 100 - 2 dec place, 1000 - 3 dec place, 10000 - 4 dec place
    print("The Average of Y: ", yAverage)

    xDifference = []
    yDifference = []

    for i in range(len(xList)): #x variable minus its average
        diff1 = xList[i] - xAverage
        diff1 = math.ceil(diff1 * 100) / 100
        xDifference.append(diff1)
    # print(xDifference)

    for i in range(len(yList)): #y variable minus its average
        diff2 = yList[i] - yAverage
        diff2 = math.ceil(diff2 * 100) / 100
        yDifference.append(diff2)
    # print(yDifference)
    
    xyProduct = []

    for i in range(len(xList)): #product of (x-xBar) and (y-yBar)
        product = xDifference[i] * yDifference[i]
        product = math.ceil(product * 100) / 100
        xyProduct.append(product)
    # print(xyProduct)

    xDifferenceRaised = []
    yDifferenceRaised = []

    for i in range(len(xList)): #x variable minus its average raised to 2
        raisedX = xDifference[i] ** 2
        raisedX = math.ceil(raisedX * 100) / 100
        xDifferenceRaised.append(raisedX)
    # print(xDifferenceRaised)
    
    for i in range(len(yList)): #y variable minus its average raised to 2
        raisedY = yDifference[i] ** 2
        raisedY = math.ceil(raisedY * 100) / 100
        yDifferenceRaised.append(raisedY)
    # print(yDifferenceRaised)

    xyProductSum = sum(xyProduct) #summation of product of (x-xBar) and (y-yBar)
    xyProductSum = math.ceil(xyProductSum * 100) / 100
    # print(xyProductSum)
    xDifferenceRaisedSum = sum(xDifferenceRaised) #summation of x variable minus its average raised to 2
    xDifferenceRaisedSum = math.ceil(xDifferenceRaisedSum * 100) / 100
    # print(xDifferenceRaisedSum)
    yDifferenceRaisedSum = sum(yDifferenceRaised)
    yDifferenceRaisedSum = math.ceil(yDifferenceRaisedSum * 100) / 100

    slope = xyProductSum / xDifferenceRaisedSum #getting the slope
    slope = math.ceil(slope * 1000) / 1000
    print("The Slope is: ", slope)

    yIntercept = yAverage - (slope * xAverage) #getting the y-intercept
    yIntercept = math.ceil(yIntercept * 1000) / 1000
    print("The Y-intercept is: ", yIntercept)

    yPredicted = []
    
    for i in range(len(xNewList)):
        predicted = (slope * xNewList[i]) + yIntercept #getting the Y-Predicted
        predicted = math.ceil(predicted * 1000) / 1000
        yPredicted.append(predicted)
    
    yPredictedDifference = []
    
    for i in range(len(yList)): #y-predicted minus y Average
        diff3 = yPredicted[i] - yAverage
        diff3 = math.ceil(diff3 * 100) / 100
        yPredictedDifference.append(diff3)
    
    yPredictedDifferenceYAverageSquared = []
    
    for i in range(len(xNewList)): #getting the squared of y-predicted minus y Average
        differenceAverage = yPredictedDifference[i] ** 2
        differenceAverage = math.ceil(differenceAverage * 1000) / 1000
        yPredictedDifferenceYAverageSquared.append(differenceAverage)
    
    # print(sum(yPredictedDifferenceYAverageSquared))
    # print(yDifferenceRaisedSum)
    
    rSquared = sum(yPredictedDifferenceYAverageSquared) / sum(yDifferenceRaised)
    rSquared = math.ceil(rSquared * 1000) / 1000
    print("The R-Squared is: ", rSquared)
    
    return yPredicted

# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = [2, 3, 2, 5, 4, 5, 9]
# data = list(range(1, 8, 1))
data = list(range(100000, 102500, 1))

csvData = read_csv("ML_Activity1.csv") #Reading the CSV File

number = csvData['Item No.'].tolist() #Number of rows
xHistoricalDataList = csvData['X'].tolist() #X variable data
yHistoricalDataList = csvData['Y'].tolist() #Y variable data

# print("\nThe Y-predicted Values are: ", regressionAnalysis(list1, list2, data))
print("\nThe Y-predicted Values are: ", regressionAnalysis(xHistoricalDataList, yHistoricalDataList, data)) #Calling the function for regression

