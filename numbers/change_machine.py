"""Change Return Program
The user enters a cost and then the amount of money given. The program will 
figure out the change and the number of quarters, dimes, nickels, pennies 
needed for the change.
"""

def main():
    print("Change Machine")
    while True:
        cost = getInput("cost", "Enter the cost: ")
        if cost == 0:
            break
        
        given = getInput("money given", "Enter the money given: ")
        if given == 0:
            break
        
        cost = cost - given
        [quarters, dimes, nickels, pennies] = calculateChange(cost)
        print("You have %d quarters, %d dimes, %d nickels, and %d pennies left" %
              (quarters, dimes, nickels, pennies))
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

def calculateChange(cost):
    cost = cost * 100 # convert to pennies
    quarters = int(cost / 25)
    dimes = int((cost % 25) / 10)
    nickels = int(((cost % 25) % 10) / 5)
    pennies = int(cost % 25 % 10 % 5)
    return [quarters, dimes, nickels, pennies]

if __name__ == "__main__":
    main()