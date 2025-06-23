import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate π/2 using mpmath's pi constant
pi_half = mp.pi / 2

# Calculate the rational term 5/3 with high precision
rational_term = mp.mpf(5)/3

# Combine the components for final result
result = pi_half - rational_term

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))