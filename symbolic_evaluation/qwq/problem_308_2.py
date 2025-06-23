import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute natural logarithm term: ln(1 + sqrt(2))
log_argument = 1 + sqrt2
log_term = mp.log(log_argument)

# Multiply logarithm term by 3
three_log_term = 3 * log_term

# Final calculation: 3*ln(1+sqrt2) - sqrt2
result = three_log_term - sqrt2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))