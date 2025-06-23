import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute 2 + sqrt(5)
two_plus_sqrt5 = 2 + sqrt5

# Calculate natural logarithm of (2 + sqrt(5))
log_term = mp.log(two_plus_sqrt5)

# Cube the logarithmic term
log_cubed = log_term ** 3

# Multiply by 1/6 to get final result
result = log_cubed / 6

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))