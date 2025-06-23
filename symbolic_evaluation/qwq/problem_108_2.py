import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by 17
seventeen_sqrt2 = 17 * sqrt2

# Multiply by pi
numerator = seventeen_sqrt2 * mp.pi

# Divide by 30 to get the final result
result = numerator / 30

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))