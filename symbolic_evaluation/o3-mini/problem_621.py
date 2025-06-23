import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi constant
pi_val = mp.pi

# Compute half of pi
half_pi = pi_val / 2

# Apply negative sign to get the result
result = -half_pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))