import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi constant
pi = mp.pi

# Compute pi cubed
pi_cubed = pi ** 3

# Calculate first term: (π³)/8
term1 = pi_cubed / 8

# Calculate second term: π
term2 = pi

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))