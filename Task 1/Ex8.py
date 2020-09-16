numOfWidgets = int(input ("Enter your number of widgets: "))
numofGizmos = int(input ("Enter your number of Gizmos: "))

weightOfWidgets = numOfWidgets * 75
weightOfGizmos = numofGizmos * 112

totalWeight = weightOfGizmos + weightOfWidgets

convert = str(totalWeight)

print ("The total weight of the order is " + convert)
