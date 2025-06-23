import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate each term separately with intermediate variables
pi = mp.pi
sqrt3 = mp.sqrt(3)

# First term: π³/288
pi_cubed = pi ** 3
term1 = pi_cubed / mp.mpf(288)

# Second term: -π√3/48
term2 = -(pi * sqrt3) / mp.mpf(48)

# Third term: π/16
term3 = pi / mp.mpf(16)

# Fourth term: -1/16
term4 = -mp.mpf(1)/mp.mpf(16)

# Combine all terms
result = term1 + term2 + term3 + term4

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))