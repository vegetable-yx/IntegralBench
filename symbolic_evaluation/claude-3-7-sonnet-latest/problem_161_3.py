import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sinh(1) and cosh(1)
sinh_val = mp.sinh(1)
cosh_val = mp.cosh(1)

# Compute 12 * sinh(1)
term1 = 12 * sinh_val

# Compute 8 * cosh(1)
term2 = 8 * cosh_val

# Combine the terms: 12*sinh(1) - 8*cosh(1)
result = term1 - term2

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))