import mpmath as mp
mp.dps = 15

# Direct assignment of the exact integer value
result = mp.mpf(17)

# Print result with 10 decimal places (will show .0000000000)
print(mp.nstr(result, n=10))