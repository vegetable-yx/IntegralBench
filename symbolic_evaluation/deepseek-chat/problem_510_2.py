import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: pi multiplied by the square root of 3
numerator = mp.pi * mp.sqrt(3)

# Divide the numerator by 9 to get the final result
result = numerator / 9

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))