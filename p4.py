# Find the largest palindrome made from the product of two 3-digit numbers.
# first task: create a palindrome checker
# to find the actual answer i went through the list manually, not the most elegant of solutions
n1 = 100
n2 = 100
biggest = 0
product = 0
while n2 < 1000:
    n1 = 100
    while n1 < 1000:
        p = n1 * n2
        product = str(p)
        plength = int(len(product))
        if plength % 6 == 0:
            if int(product[0]) == int(product[5]):
                if int(product[1]) == int(product[4]):
                    if int(product[2]) == int(product[3]):
                        if p > biggest:
                            biggest = p
        n1 = n1 + 1
    n2 = n2 + 1
print(str(biggest))
