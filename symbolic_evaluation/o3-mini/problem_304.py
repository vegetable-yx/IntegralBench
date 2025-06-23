import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute the constant sqrt(3)
sqrt3 = mp.sqrt(3)

# Compute the natural logarithm argument: (sqrt(3) + 1) / 2
log_arg = (sqrt3 + 1) / 2

# Compute the logarithm: ln((sqrt(3)+1)/2)
log_val = mp.log(log_arg)

# Compute the expression inside the parentheses: 8 - 3*pi + 6*log_val
inner_expr = 8 - 3*mp.pi + 6*log_val

# Multiply by sqrt(3) and divide by 8
result = (sqrt3 * inner_expr) / 8

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))