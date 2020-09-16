WINDCHILL_OFFSET = 13.12
WINDCHILL_FACTOR1 = 0.6215
WINDCHILL_FACTOR2 = -11.37
WINDCHILL_FACTOR3 = 0.3965
WINDCHILL_EXP = 0.16

temp = float(input("Enter the air temperature in (degrees Celsius): "))
speed = float(input("Enter the wind speed (kilometer per hour): "))

wci = WINDCHILL_OFFSET + (WINDCHILL_FACTOR1 * temp) + (WINDCHILL_FACTOR2 * speed ** WINDCHILL_EXP) + (
            WINDCHILL_FACTOR3 * temp * speed ** WINDCHILL_EXP)

print("Your Wind Chill Index ",round(wci,1))