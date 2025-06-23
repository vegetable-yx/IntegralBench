import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate -3π using mpmath's pi constant
pi_value = mp.pi
three_pi = 3 * pi_value
result = -three_pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))