import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π^3
pi_cubed = mp.pi ** 3

# Compute first term: π³/48
term1 = pi_cubed / 48

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Compute second term: (π/4) * ln2
term2 = (mp.pi / 4) * ln2

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))