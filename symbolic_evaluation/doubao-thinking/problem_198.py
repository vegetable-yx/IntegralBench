import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate 2*π using mpmath's pi constant
two_pi = 2 * mp.pi

# Compute the square root of 2π using mpmath's sqrt function
result = mp.sqrt(two_pi)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))