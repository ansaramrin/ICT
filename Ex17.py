HEAT_CAPACITY = 4.186
J_TO_KWH = 2.777e-7

volume = float(input("Enter amount of water in milliliters: "))
temp = float(input("Enter amount of temperature increase (degrees Celsius): "))
price = float(input("Enter electricity cost per unit: "))

energy = volume * temp * HEAT_CAPACITY
kwh = energy * J_TO_KWH
cost = kwh * price

print("Amount of energy needed ", round(energy, 2), "Joules, which will cost", round(cost, 2))