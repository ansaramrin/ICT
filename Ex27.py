height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))
height1= float(input("Enter your height in inches: "))
weight2 = float(input("Enter your weight in pounds: "))

bmi1 = weight / (height*height)
bmi2= (weight / (height*height))*703
print("Your Body Mass Index is:",bmi1)
print("Your Body Mass Index is:",bmi2)