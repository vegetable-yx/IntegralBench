import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply by pi to get final result
result = mp.pi * sqrt_2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))