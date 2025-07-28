def isPrime(number):
    if number == 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def printAllPrimes(limit):
    res = []
    for i in range(2, limit+1):
        if isPrime(i):
            res.append(str(i))
        
    print(" ".join(res))