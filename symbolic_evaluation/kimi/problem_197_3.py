import mpmath as mp
mp.dps = 15

# Calculate π^2 using mpmath constant
pi_squared = mp.pi ** 2

# Compute first term: π² divided by 16
term1 = pi_squared / 16

# Compute second term: 1 divided by 4
term2 = mp.mpf(1)/4

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))