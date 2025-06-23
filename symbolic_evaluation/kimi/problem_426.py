import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute π using mpmath constant
pi_value = mp.pi

# Calculate π/4
pi_over_4 = pi_value / 4

# Add 1 to π/4
result = 1 + pi_over_4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))