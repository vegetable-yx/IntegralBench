import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the first term: (sqrt(3) * π)/8
sqrt3 = mp.sqrt(3)
term1 = (sqrt3 * mp.pi) / 8

# Calculate the second term: π²/24
pi_squared = mp.pi ** 2
term2 = pi_squared / 24

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))