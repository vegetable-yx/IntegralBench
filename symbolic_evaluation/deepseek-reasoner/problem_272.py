import mpmath as mp
mp.dps = 15  # Set internal precision

# Compute square root of 2
sqrt2 = mp.sqrt(2)

# Calculate components for logarithmic term
log_numerator = sqrt2 + 1  # sqrt(2) + 1
log_argument = log_numerator / 2  # (sqrt(2) + 1)/2

# Compute natural logarithm of the argument
log_term = mp.log(log_argument)

# Combine all components in the parentheses
parentheses_content = sqrt2 - 1 - log_term

# Multiply by pi/2 for final result
result = (mp.pi / 2) * parentheses_content

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))