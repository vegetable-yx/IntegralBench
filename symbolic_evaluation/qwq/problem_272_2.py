import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute the argument for the logarithm
log_numerator = sqrt2 + 1
log_argument = log_numerator / 2

# Calculate the logarithmic term
log_term = mp.log(log_argument)

# Combine all components in the parentheses
parentheses_content = sqrt2 - 1 - log_term

# Multiply by pi/2 for final result
result = (mp.pi / 2) * parentheses_content

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))