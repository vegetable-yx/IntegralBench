import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute pi constant
pi_val = mp.pi

# Calculate pi/4
pi_over_4 = pi_val / 4

# Subtract 1/2 from pi/4
result = pi_over_4 - mp.mpf('0.5')

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))