import mpmath as mp
mp.dps = 15

# Calculate the square root of 2
sqrt_2 = mp.sqrt(2)

# Compute the reciprocal of sqrt(2)
result = 1 / sqrt_2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))