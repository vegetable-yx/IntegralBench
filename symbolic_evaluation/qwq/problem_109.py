import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Get mathematical constants
pi_value = mp.pi
catalan_constant = mp.catalan

# Calculate π * Catalan constant
result = pi_value * catalan_constant

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))