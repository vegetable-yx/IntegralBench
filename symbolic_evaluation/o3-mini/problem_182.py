import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the argument for the logarithm: (2 + sqrt(5))
log_arg = 2 + sqrt5

# Calculate the natural logarithm of the argument
log_value = mp.log(log_arg)

# Compute the expression inside the parentheses: log_value + 1 - sqrt5
inner_expr = log_value + 1 - sqrt5

# Multiply by pi to get the final result
result = mp.pi * inner_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))