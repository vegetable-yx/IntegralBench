import mpmath as mp
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π/2
result = pi_value / 2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))