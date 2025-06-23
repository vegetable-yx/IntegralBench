import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant e (base of natural logarithm)
e_val = mp.e

# Calculate the inner expression: (e - 1)
inner_expr = e_val - 1

# Compute exp(e - 1)
exp_result = mp.exp(inner_expr)

# Subtract e from the result
result = exp_result - e_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))