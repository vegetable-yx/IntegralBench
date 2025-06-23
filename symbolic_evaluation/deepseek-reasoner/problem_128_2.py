import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate 2π using mpmath's pi constant
result = 2 * mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))