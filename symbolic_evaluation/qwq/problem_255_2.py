import mpmath as mp
mp.dps = 15

# Calculate -3π using mpmath's high-precision pi constant
result = -3 * mp.pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))