import mpmath as mp

mp.dps = 15  # Set decimal precision for intermediate calculations

# Calculate π squared
pi_sq = mp.pi ** 2

# Compute first term: π²/32
term1 = pi_sq / 32

# Calculate arcsin(1/4) using mpmath's asin function
arcsin_val = mp.asin(0.25)

# Square the arcsin result
arcsin_sq = arcsin_val ** 2

# Compute second term: 0.5 * (arcsin(1/4))²
term2 = 0.5 * arcsin_sq

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))