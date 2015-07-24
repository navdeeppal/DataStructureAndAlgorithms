
######### Chapter 8, Program exercise 3
# This Program determines how long it takes for an investment to double at a given interest rate.

initialDeposit = eval(input("Please enter your Investment: "))
intRatePer = eval(input("Please enter Annual Interest Rate in percentage: "))
intRate = intRatePer/100
finalDeposit = initialDeposit
doubleYears = 0
while finalDeposit <= 2*initialDeposit:
    finalDeposit = finalDeposit + (intRate*finalDeposit)
    doubleYears = doubleYears+1
print("Number of years to double the investment:", doubleYears)
    