import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate hyperbolic sine and cosine components
sinh_4 = mp.sinh(4)
cosh_4 = mp.cosh(4)

# Compute the terms with their coefficients
term1 = 348 * sinh_4
term2 = 295 * cosh_4

# Combine all components according to the formula
numerator = term1 - term2 + 175
result = numerator / 32

# Print the final result with 10 decimal places precision
print(mp.nstr(result, n=10))