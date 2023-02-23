n = 57

for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not a prime number, it is divisible by {i}")
        break
else:
    print(f"{n} is a prime number")
