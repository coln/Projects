"""Mortgage Calculator
Calculate the monthly payments of a fixed term mortgage over given Nth terms 
at a given interest rate. Also figure out how long it will take the user to 
pay back the loan.
"""

def main():
    print("Mortgage Calculator")
    while True:
        print("Enter '0' to quit")
        principal = getInput("principal", "Enter your principal: ")
        if principal == 0:
            break
        
        interest = getInput("interest", "Enter your annual interest rate: ")
        if interest == 0:
            break
        
        years = getInput("years", "Enter the number of years to repay: ")
        if years == 0:
            break
        
        monthlyPayments = calculateMontlyPayments(principal, interest, years)
        monthsLeft = calculateMonthsUntilPaid(principal, interest, years)
        totalCost = calculateTotalCost(monthlyPayments, monthsLeft)
        print("You have %d months left of $%.2f payments" % (monthsLeft, monthlyPayments))
        print("Total cost of loan: %.2f" % totalCost)
        print("")

def getInput(name, input_msg):
    number = -1
    while True:
        number = input(input_msg)
        try:
            number = float(number)
        except ValueError:
            print("Invalid " + name)
            continue
        
        if number < 0.0:
            print(name.title() + " must be a positive number")
            continue
        break
    return number

def calculateMontlyPayments(principal, interest, years):
    """http://www.hughcalc.org/formula.php
    """
    monthlyInterest = interest / 12
    months = years * 12
    return principal * (monthlyInterest / (1 - (1 + monthlyInterest) ** -months))

def calculateMonthsUntilPaid(principal, interest, years):
    """http://www.hughcalc.org/formula.php
    """
    monthlyInterest = interest / 12
    months = years * 12
    monthlyPayments = calculateMontlyPayments(principal, interest, years)
    
    totalMonths = 0
    balance = principal
    while balance > 0:
        currentInterest = principal * monthlyInterest
        currentPrincipal = monthlyPayments - currentInterest
        balance -= currentPrincipal
        if balance > 0:
            totalMonths += 1
    
    return totalMonths

def calculateTotalCost(monthlyPayments, monthsLeft):
    return monthlyPayments * monthsLeft

if __name__ == "__main__":
    main()