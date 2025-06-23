import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi^3
pi_cubed = mp.pi ** 3

# Compute first term: π³/12
term1 = pi_cubed / 12

# Compute second term: 11π/16
term2 = (11 * mp.pi) / 16

# Combine terms: π³/12 - 11π/16
result = term1 - term2

# Print final result to 10 decimal places
print(mp.nstr(result, n=10))