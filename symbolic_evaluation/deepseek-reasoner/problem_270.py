import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate π^3 component
pi_cubed = mp.pi ** 3

# Calculate first term: π^3 / 192
term1 = pi_cubed / 192

# Calculate second term: π / 128
term2 = mp.pi / 128

# Combine terms for final result
result = term1 - term2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))