import mpmath as mp
mp.dps = 15
# Calculate natural logarithm of 3
result = mp.log(3)
print(mp.nstr(result, n=10))