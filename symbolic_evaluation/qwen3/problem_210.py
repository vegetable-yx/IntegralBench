import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π^3
pi_cubed = mp.pi ** 3

# Calculate first term: π^3 / 8
term1 = pi_cubed / 8

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Calculate second term: π * ln2
term2 = mp.pi * ln2

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))