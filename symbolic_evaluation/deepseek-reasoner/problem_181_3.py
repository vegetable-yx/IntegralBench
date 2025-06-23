import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π divided by 16
result = pi_value / 16

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))