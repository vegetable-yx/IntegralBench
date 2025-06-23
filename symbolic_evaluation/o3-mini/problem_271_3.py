import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the constant pi
pi = mp.pi

# Calculate numerator: 19 times pi
numerator = 19 * pi

# Calculate the result: numerator divided by 512
result = numerator / 512

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))