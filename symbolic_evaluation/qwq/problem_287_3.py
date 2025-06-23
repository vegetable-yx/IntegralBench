import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate intermediate constants
sqrt2 = mp.sqrt(2)  # Compute square root of 2
ln_term = mp.log(1 + sqrt2)  # Natural logarithm of (1 + √2)

# Compute components of the final expression
term1 = (mp.pi / 8) * (ln_term ** 2)  # First term: π/8 * (ln(1+√2))²
term2 = (mp.pi / 24) * (ln_term ** 3)  # Second term: π/24 * (ln(1+√2))³

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))