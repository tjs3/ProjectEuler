# What is the largest prime factor of the number 600851475143 ?
n = 600851475143
if n > 1:
    print("You asked for the prime factorisation of " + str(n) + ", here is is: ")
    i = n
    d = n
    j = 2
    while d > 1:
        if d % j == 0:
            print(str(j))
            print("*")
            d = d / j
        else:
            # print("no factor")
            j += 1
    print("1\n= " + str(n))
else:
    print("Don't be silly.")
