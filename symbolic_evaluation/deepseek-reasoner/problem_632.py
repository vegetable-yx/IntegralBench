import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate natural logarithm of 2
log_two = mp.log(2)

# Compute the final result by negating the logarithm
result = -log_two

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))