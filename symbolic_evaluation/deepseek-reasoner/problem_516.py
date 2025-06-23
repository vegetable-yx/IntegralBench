import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi constant
pi_val = mp.pi

# Calculate pi divided by 2
half_pi = pi_val / 2

# Subtract 1 from pi/2
result = half_pi - 1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))