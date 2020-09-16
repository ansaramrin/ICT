kpa = float(input("Input pressure in in kilopascals:"))
psi = kpa / 6.89475729
mmhg = kpa * 760 / 101.325
atm = kpa / 101.325
print("The pressure in pounds per square inch:",round(psi,2))
print("The pressure in millimeter of mercury:",round(mmhg,2))
print("Atmosphere pressure:",round(atm,2))