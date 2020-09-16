in_bal=int(input("Initial balance is:"))
ad_bal=4
bal_1year=in_bal+(in_bal*4/100)
bal_2year=bal_1year+(in_bal*4/100)
bal_3year=bal_2year+(in_bal*4/100)
print("Total balance in 1 year is",round(bal_1year,2))
print("Total balance in 2 year is",round(bal_2year,2))
print("Total balance in 3 year is",round(bal_3year,2))