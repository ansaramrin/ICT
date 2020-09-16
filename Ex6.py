price_meal=float(input("Write the price of the meal:"))
print("Tip amount is 18%")
print("Tax amount is 15%")
tip = price_meal+price_meal*18/100
tax = price_meal+price_meal*15/100
total_price = price_meal + tip + tax
print("Total price is:",round(total_price,2),"$")