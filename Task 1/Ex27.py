height_in_meters = float(input("Enter your height in meters: "))
weight_in_kgs = float(input("Enter your weight in kg: "))
height_in_inches= float(input("Enter your height in inches: "))
weight_in_pounds = float(input("Enter your weight in pounds: "))

BMI1 = (weight_in_pounds / (height_in_inches*height_in_inches))*703
BMI2 = weight_in_kgs / (height_in_meters*height_in_meters)

print("Your Body Mass Index is:",BMI1)
print("Your Body Mass Index is:",BMI2)