import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 11
sqrt_11 = mp.sqrt(11)

# Multiply the square root by 11
numerator = 11 * sqrt_11

# Divide the result by 18
result = numerator / 18

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))