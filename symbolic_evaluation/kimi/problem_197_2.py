import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π^2
pi_squared = mp.pi ** 2

# Compute first term: π²/16
term1 = pi_squared / 16

# Compute second term: 1/4
term2 = mp.mpf(1)/4

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))