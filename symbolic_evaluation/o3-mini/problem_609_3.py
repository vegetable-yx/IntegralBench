import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate the constant pi
pi_val = mp.pi

# Compute pi divided by 2
pi_over_2 = pi_val / 2

# Calculate the result: 1 - pi/2
result = mp.mpf(1) - pi_over_2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))