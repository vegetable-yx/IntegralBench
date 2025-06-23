import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute 2 * π using mpmath's constant for pi
result = 2 * mp.pi

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))