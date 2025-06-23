import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the square root of 2
sqrt_val = mp.sqrt(2)

# Compute 1 + sqrt(2)
inner_expr = 1 + sqrt_val

# Calculate natural logarithm of (1 + sqrt(2))
log_val = mp.log(inner_expr)

# Compute π/2
pi_over_2 = mp.pi / 2

# Multiply π/2 by the logarithm to get the final result
result = pi_over_2 * log_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))