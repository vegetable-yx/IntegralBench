import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sqrt(2) using mpmath's square root function
sqrt_val = mp.sqrt(2)

# Compute 1 + sqrt(2)
sum_val = 1 + sqrt_val

# Calculate natural logarithm of (1 + sqrt(2))
log_val = mp.log(sum_val)

# Square the logarithm value
log_squared = log_val ** 2

# Multiply by pi and divide by 8 to get final result
result = (mp.pi / 8) * log_squared

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))