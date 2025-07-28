def list_factors(n):
    res = []
    for i in range(1, n+1):
        if n % i == 0:
            res.append(str(i))

    return " ".join(res) + " "

def find_sum_and_num_factors(n):
    res = []
    for i in range(1, n+1):
        if n % i == 0:
            res.append(str(i))

    return " ".join(res) + " "

def isPrime(number):
    if number == 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True

num = int(input("Enter positive number: "))
fsum, fcount = find_sum_and_num_factors(num)

print(f"Factors of {num} are")
print(list_factors(num))
print(f"Sum of {list_factors(num)}is {fsum}")
print(f"Number of factors is {fcount}")

if isPrime(num):
    print(f"{num} is prime number.")
else:
    print(f"{num} is not prime number.")