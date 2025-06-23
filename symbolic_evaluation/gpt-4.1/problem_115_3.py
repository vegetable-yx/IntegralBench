import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the argument for the logarithm: 1 + sqrt(2)
arg = 1 + mp.sqrt(2)

# Compute the natural logarithm: ln(1 + sqrt(2))
log_val = mp.log(arg)

# Compute hyperbolic cosine: cosh(ln(1 + sqrt(2)))
cosh_val = mp.cosh(log_val)

# Compute hyperbolic sine: sinh(ln(1 + sqrt(2)))
sinh_val = mp.sinh(log_val)

# Compute the inner expression: ln(1+sqrt(2)) * cosh(...) - sinh(...)
inner_expr = log_val * cosh_val - sinh_val

# Multiply by 2 to get the final result
result = 2 * inner_expr

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))