import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate 4*sqrt(3)
sqrt_term = mp.sqrt(3)
multiplied_sqrt = 4 * sqrt_term

# Calculate 2*pi/3
pi_term = (2 * mp.pi) / 3

# Combine both terms
result = multiplied_sqrt + pi_term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))