import mpmath as mp
mp.dps = 15

# Calculate -3π using mpmath's pi constant
result = -3 * mp.pi

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))