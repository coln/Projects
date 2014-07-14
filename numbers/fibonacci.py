def main():
    while True:
        print("Please select a choice:")
        print("   1) Generate Fibonacci sequence up to a number N")
        print("   2) Generate the Nth Fibonacci number")
        print("   0) Quit")
        choice = input("Choice: ")
        choice = int(choice)
        if choice in (1, 2):
            n = input("Enter a number: ")
            n = int(n)
            if n <= 0:
                print("Invalid number")
                continue
        
        if choice == 0:
            break
        elif choice == 1:
            print("Fibonacci sequence up to ", n)
            fibonacciUpTo(n)
            break
        elif choice == 2:
            numberWord = getNumberWord(n)
            msg = "The " + numberWord
            msg += " fibonacci number is: "
            msg += str(nthFibonacci(n))
            print(msg)
            break
        else:
            print("Sorry, invalid choice.")

def getNumberWord(number):
    word = str(number)
    last = word[-1:]
    if last == "1":
        word += "st"
    elif last == "2":
        word += "nd"
    elif last == "3":
        word += "rd"
    else:
        word += "th"
    return word

def fibonacciUpTo(n):
    prev = 0
    fib = 1
    while fib < n:
        print(fib, end=" ")
        fib, prev = (prev + fib), fib
    print("")

def nthFibonacci(n):
    count = 0
    prev = 1
    fib = 1
    while count < n:
        fib, prev = (prev + fib), fib
        count += 1
    return fib

if __name__ == "__main__":
    main()