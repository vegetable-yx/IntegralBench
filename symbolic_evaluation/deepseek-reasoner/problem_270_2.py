import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute fundamental constants
sqrt3 = mp.sqrt(3)
pi = mp.pi

# Calculate powers of pi used in multiple terms
pi_squared = pi ** 2
pi_cubed = pi ** 3

# Compute individual terms of the expression
term1 = pi_cubed / 192                # π³/192 component
term2 = (-7 * sqrt3 * pi_squared) / 384  # -7√3π²/384 component
term3 = (-19 * pi) / 256              # -19π/256 component
term4 = 15 / 256                      # Constant term 15/256

# Combine all terms for final result
result = term1 + term2 + term3 + term4

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))