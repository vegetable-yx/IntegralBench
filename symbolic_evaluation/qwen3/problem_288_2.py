import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate ln(1 + sqrt(2))
sqrt2 = mp.sqrt(2)
ln_arg = 1 + sqrt2
ln_val = mp.log(ln_arg)

# Compute squared logarithm term
ln_squared = ln_val ** 2

# Calculate pi^2 / 24
pi_sq_over_24 = (mp.pi ** 2) / 24

# Combine all components inside the parentheses
inner_expression = ln_squared - ln_val + pi_sq_over_24 - 0.5

# Multiply by pi/16 to get final result
result = (mp.pi / 16) * inner_expression

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))