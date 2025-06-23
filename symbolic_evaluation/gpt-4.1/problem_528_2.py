import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the mathematical constant e
e_constant = mp.e

# Calculate the inner expression: (e - 1)
inner_expr = e_constant - 1

# Compute e raised to the power of (e - 1)
exp_term = mp.exp(inner_expr)

# Subtract e from the result
result = exp_term - e_constant

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))