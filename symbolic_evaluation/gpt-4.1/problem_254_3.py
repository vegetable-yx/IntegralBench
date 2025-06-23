import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the value of -3π using mpmath's pi constant
result = -3 * mp.pi

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))