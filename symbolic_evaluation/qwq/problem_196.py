import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π²/48
pi_squared = mp.pi ** 2
term1 = pi_squared / 48

# Calculate (π√3)/6
pi_times_sqrt3 = mp.pi * mp.sqrt(3)
term2 = pi_times_sqrt3 / 6

# Calculate √3/2
term3 = mp.sqrt(3) / 2

# Combine all terms: π²/48 - (π√3)/6 + √3/2
result = term1 - term2 + term3

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))