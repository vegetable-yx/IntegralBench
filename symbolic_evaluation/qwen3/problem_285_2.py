import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute 1 + sqrt(2)
inner_value = 1 + sqrt2

# Calculate natural logarithm of (1 + sqrt(2))
log_term = mp.log(inner_value)

# Cube the logarithmic term
log_cubed = log_term ** 3

# Divide by 6 to get final result
result = log_cubed / 6

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))