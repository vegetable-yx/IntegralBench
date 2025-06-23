import mpmath as mp
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by pi to get the final result
result = mp.pi * sqrt2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))