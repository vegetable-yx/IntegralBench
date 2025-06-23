import mpmath as mp
mp.dps = 15

# Assign the exact integer value directly
result = mp.mpf(18)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))