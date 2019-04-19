# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
i = 2*2*2*2*3*3*5*7*11*13*17*19
print("candidate = " + str(i))
c = 20
q = int(input("test"))


while c > 0:
    if q % c == 0:
        print(str(q) + " div by " + str(c))
    c = c - 1
