import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate π squared
pi_squared = mp.pi ** 2

# Calculate first term: π²/32
term1 = pi_squared / 32

# Calculate second term: 1/8
term2 = mp.mpf(1)/8

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))