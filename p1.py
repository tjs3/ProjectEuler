# Find the sum of all the multiples of 3 or 5 below 1000. Solved!
def sum_of_division_by_3_and_5(to=10):
    p_sum = 0
    for i in range(1, to):
        if i % 3 == 0 or i % 5 == 0:
            p_sum += i

    return p_sum

print(str(sum_of_division_by_3_and_5(10)))
