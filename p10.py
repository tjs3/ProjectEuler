import time
start = time.time()
print("This program will sum primes less than n.")
# n = int(input("please choose your n:\n "))
n = 2000000
sum_of_primes = 0
primes = []
for i in range(0, n):   # creates an array big enough, 0 is list[0], 1 is list[1]
    primes.append(True)  # True means prime
primes[0] = False
primes[1] = False
for i in range(0, n):
    if primes[i]:
        m = 0
        j = i * i
        while j < n:
            primes[j] = False  # crossing out of non primes
            j += i
for i in range(0, n - 1):     # sums the primes left in the table
    if primes[i]:
        sum_of_primes = sum_of_primes + i
print("\nsum of primes: " + str(sum_of_primes))
end = time.time()
print("\ntime taken:\n" + str(end - start))
