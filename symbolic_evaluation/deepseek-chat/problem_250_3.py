import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Subtract 1 from the square root of 2
sqrt2_minus_1 = sqrt2 - 1

# Multiply by pi to get the final result
result = mp.pi * sqrt2_minus_1

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))