import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate π³
pi_cubed = mp.power(mp.pi, 3)

# Calculate first term: π³ / 8
term1 = pi_cubed / 8

# Calculate the dilogarithm term: Li₂(0.0625)
dilog_term = mp.polylog(2, 0.0625)

# Calculate second term: (π / 2) * Li₂(0.0625)
term2 = (mp.pi / 2) * dilog_term

# Combine the terms: result = term1 - term2
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))