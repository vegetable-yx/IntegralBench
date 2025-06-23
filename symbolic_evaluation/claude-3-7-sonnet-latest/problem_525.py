import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate pi/4
pi_over_4 = mp.pi / 4

# Calculate 1/2
half = mp.mpf(1) / 2

# Compute the result: π/4 - 1/2
result = pi_over_4 - half

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))