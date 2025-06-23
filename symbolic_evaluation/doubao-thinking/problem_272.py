import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute the logarithm argument (1 + sqrt(2))/2
log_arg = (1 + sqrt2) / 2

# Calculate the logarithm term
log_term = mp.log(log_arg)

# Combine all components: sqrt(2) - 1 - log_term
combined = sqrt2 - 1 - log_term

# Multiply by pi/2 to get final result
result = (mp.pi / 2) * combined

# Print result with 10 decimal places
print(mp.nstr(result, n=10))