import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Compute the expression inside the logarithm: 4 - 2*sqrt(3)
inner_expr = 4 - 2 * sqrt3

# Compute the natural logarithm of the inner expression
log_val = mp.log(inner_expr)

# Calculate the constant factor: pi/6
pi_over_6 = mp.pi / 6

# Multiply to get the final result
result = pi_over_6 * log_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))