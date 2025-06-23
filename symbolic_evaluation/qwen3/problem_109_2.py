import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root components
sqrt2 = mp.sqrt(2)
sqrt3 = mp.sqrt(3)

# Compute the argument for the logarithm
log_numerator = 1 + sqrt3
log_denominator = sqrt2
log_argument = log_numerator / log_denominator

# Calculate the natural logarithm term
log_term = mp.log(log_argument)

# Combine all components for final result
pi_component = mp.pi
result = pi_component * sqrt2 * log_term

# Output result with 10 decimal precision
print(mp.nstr(result, n=10))