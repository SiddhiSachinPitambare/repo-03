def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"
print(prime(6))
print(prime(15))
print(prime(16))
print(prime(18))
print(prime(27))