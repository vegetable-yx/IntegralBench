import mpmath as mp
mp.dps = 15

# Assign the exact integer value to result
result = mp.mpf(99)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))