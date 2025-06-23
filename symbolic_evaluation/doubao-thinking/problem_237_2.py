import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate 3π using mpmath's pi
result = 3 * mp.pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))