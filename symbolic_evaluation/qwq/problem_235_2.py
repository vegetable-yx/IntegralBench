import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Compute the first term components
pi_term = mp.pi
numerator = 32 * sqrt3 * pi_term
term1 = numerator / 27

# Compute the second term
term2 = mp.mpf(5) / 6  # Convert integers to mpmath floats

# Combine both terms
result = term1 + term2

# Print final result with 10 decimal precision
print(mp.nstr(result, n=10))