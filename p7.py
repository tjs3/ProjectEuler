# What is the 10 001st prime number?
import math
import time
start_time = time.time()
c = 4
i = 2
p = False
# 2, 3, 5, 7
# create some function which assigns true or false to p depending on whether n is prime or or not
while c < 10001:
    n = 6*i - 1
# test for n_one and set a value for p
# start of test for prime
    j = 2
    p = True
    while p and j - 1 < int(math.sqrt(n + 1)):
        if n % j != 0:
            p = True
        else:
            p = False
        j += 1
# end of test for prime
    if p:
        c += 1
    p = False
    if c < 10001:
        n = 6*i + 1
        # test for n_two and set a value for p
        # start of test for prime
        j = 2
        p = True
        while p and j - 1 < int(math.sqrt(n + 1)):
            if n % j != 0:
                p = True
            else:
                p = False
            j += 1
        # end of test for prime
        if p:
            c += 1
    i += 1
print(str(n))
print("\nRuntime: \n%s seconds" % (time.time() - start_time))
