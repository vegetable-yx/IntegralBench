import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Compute the difference (sqrt(2) - 1)
difference = sqrt_2 - 1

# Multiply by pi to get final result
result = mp.pi * difference

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))