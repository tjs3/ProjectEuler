n = 100
sos = ((n*n)*((n+1)*(n+1)))/4
other = ((n)*((n+1)*((2*n)+1)))/6
diff = abs(other - sos)
print(str(diff))
