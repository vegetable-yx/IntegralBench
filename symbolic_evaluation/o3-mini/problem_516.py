import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi
pi_val = mp.pi

# Compute pi/2
half_pi = pi_val / 2

# Subtract 1 to get final result
result = half_pi - 1

# Print result to 10 decimal places
print(mp.nstr(result, n=10))