# By considering the terms in the Fibonacci sequence
# whose values do not exceed four million, find the
# sum of the even-valued terms.
s = 0
fn0 = 1  # first term
fn1 = 1  # second term
fn2 = 0
while fn2 < 4000000:
    fn2 = fn1 + fn0
#    print(str(fn2) + " " + str(s))
    if fn2 % 2 == 0:
        s = s + fn2
    fn0 = fn1
    fn1 = fn2
print(str(s))
