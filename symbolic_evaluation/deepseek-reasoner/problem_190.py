import mpmath as mp
mp.dps = 15

# Calculate π squared using high-precision constant
pi_squared = mp.pi ** 2

# Compute first term: π² divided by 32
term1 = pi_squared / 32

# Compute second term: 1/8 with full precision
term2 = mp.mpf(1)/8

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))