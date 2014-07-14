"""Next Prime Number
Have the program find prime numbers until the user chooses to stop asking 
for the next one.
"""

def main():
    print("Prime Number Generator")
    while True:
        print("Enter '0' to quit")
        number = input("How many prime numbers to generate? ")
        try:
            number = int(number)
        except ValueError:
            print("Invalid number")
            print("")
            continue

        if number < 0:
            print("Please enter a positive integer")
            print("")
            continue

        if number == 0:
            break

        primes = generatePrimes(number)
        print(" ".join(str(x) for x in primes))
        print("")


def generatePrimes(n):
    primes = []
    i = 3
    count = 0
    while count < n:
        i += 2
        if isPrime(i):
            primes.append(i)
            count += 1
    return primes
    
def isPrime(n):
    if n == 2:
        return True

    if n % 2 == 0:
        return False
    
    i = 3
    nSqrt = n ** 0.5
    while i < nSqrt:
        if n % i == 0:
            return False
        i += 2

    return True

if __name__ == "__main__":
    main()