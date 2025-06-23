import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π^3 term
pi_cubed = mp.pi ** 3

# Compute first term: π³/192
term1 = pi_cubed / 192

# Compute second term: π/128
term2 = mp.pi / 128

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))