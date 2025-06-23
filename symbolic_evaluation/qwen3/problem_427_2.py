import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root of 11
sqrt_11 = mp.sqrt(11)

# Multiply by 11 to get the numerator
numerator = 11 * sqrt_11

# Divide by 18 to obtain the final result
result = numerator / 18

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))