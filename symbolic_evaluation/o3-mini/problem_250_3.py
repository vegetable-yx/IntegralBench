import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt_2 = mp.sqrt(2)

# Subtract 1 from the square root
sqrt_2_minus_1 = sqrt_2 - 1

# Multiply by pi to get the final result
result = mp.pi * sqrt_2_minus_1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))