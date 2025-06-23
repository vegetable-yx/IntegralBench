import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate 2 * π using mpmath's pi constant
two_pi = 2 * mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(two_pi, n=10))