import mpmath as mp
mp.dps = 15

# Calculate π using mpmath's built-in constant
result = mp.pi

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))