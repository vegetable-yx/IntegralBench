import mpmath as mp
mp.dps = 15

# Assign the exact solution directly
result = mp.mpf(1)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))