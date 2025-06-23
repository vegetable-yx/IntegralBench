import mpmath as mp
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π divided by 2
half_pi = pi_value / 2

# Apply the negative sign to get final result
result = -half_pi

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))