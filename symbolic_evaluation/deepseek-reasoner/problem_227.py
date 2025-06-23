import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Calculate π to the fourth power
pi_fourth = pi_squared ** 2

# Compute first term: π²/16
term1 = pi_squared / 16

# Compute second term: π⁴/32
term2 = pi_fourth / 32

# Combine terms for final result
result = term1 - term2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))