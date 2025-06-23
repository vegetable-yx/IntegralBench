import mpmath as mp
mp.dps = 15

# Calculate natural logarithm of 2
result = mp.log(2)

print(mp.nstr(result, n=10))