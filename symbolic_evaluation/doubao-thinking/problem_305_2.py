import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute the argument for the natural log
log_argument = (1 + sqrt5) / 2

# Calculate the natural logarithm term
log_term = mp.log(log_argument)

# Compute the numerator: sqrt5 - 3*log_term
numerator = sqrt5 - 3 * log_term

# Final result calculation
result = numerator / 8

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))