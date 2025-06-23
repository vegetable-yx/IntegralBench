import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 11
sqrt_11 = mp.sqrt(11)

# Multiply by 11 to get the numerator
numerator = 11 * sqrt_11

# Divide by 18 to get the final result
result = numerator / 18

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))