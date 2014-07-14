def main():
    print("Prime Factorization")
    while True:
        print("Enter '0' to quit")
        number = input("Enter a number to factorize: ")
        try:
            number = int(number)
        except ValueError:
            print("The number must be an integer")
            print("")
            continue;
        
        if number == 0:
            return
        
        if number < 0:
            print("The number must be positive")
            print("")
            continue;
        
        factors = primeFactors(number)
        factors.sort()
        if len(factors):
            print("Prime factors of " + str(number) + ":")
            print(" ".join(str(x) for x in factors))
        else:
            print("The number " + str(number) + " has no prime factors")
        print("")
        

def primeFactors(number):
    factors = []
    i = 1
    while True:
        if number == 0 or number == 1:
            break
        for i in range(2, number + 1):
            if number % i != 0:
                continue
            if isPrime(i):
                factors.append(i)
                number //= i
    return factors

def isPrime(n):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True

if __name__ == "__main__":
    main()