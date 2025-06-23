import mpmath as mp

# Set the internal decimal precision to 15 digits
mp.dps = 15

# Calculate 3 times pi
numerator = 3 * mp.pi

# Divide the result by 4 to get the final value
result = numerator / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))