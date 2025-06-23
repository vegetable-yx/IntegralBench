import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sqrt(2) once for reuse
sqrt2 = mp.sqrt(2)

# Compute ln(1 + sqrt(2)) term
ln_term = mp.log(1 + sqrt2)

# Square the logarithmic term
ln_squared = ln_term ** 2

# Calculate each component of the expression
term1 = (3 * mp.pi / 16) * ln_squared
term2 = (mp.pi * sqrt2 / 8) * ln_term
term3 = mp.pi / 16

# Combine all terms to get final result
result = term1 - term2 + term3

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))