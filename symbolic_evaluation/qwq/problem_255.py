import mpmath as mp

# Set precision to 15 decimal places for calculations
mp.dps = 15

# Calculate -3π using mpmath's pi constant
pi_value = mp.pi
result = -3 * pi_value

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))