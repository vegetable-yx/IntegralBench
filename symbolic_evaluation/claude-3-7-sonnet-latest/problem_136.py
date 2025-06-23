import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply by 4
numerator = 4 * sqrt_2

# Divide by 3 to get the result
result = numerator / 3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))