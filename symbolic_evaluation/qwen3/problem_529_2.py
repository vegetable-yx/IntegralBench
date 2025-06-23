import mpmath as mp
mp.dps = 15

# Calculate the constant -π using mpmath's built-in constant
result = -mp.pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))