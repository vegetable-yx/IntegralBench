import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate intermediate values
sqrt2 = mp.sqrt(2)
inv_sqrt2 = 1 / sqrt2  # 1/√2

# Compute hyperbolic functions with intermediate values
cosh_term = mp.cosh(inv_sqrt2)
sinh_term = mp.sinh(inv_sqrt2)

# Calculate each term of the expression
term1 = sqrt2 * cosh_term
term2 = 2 * sinh_term

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))