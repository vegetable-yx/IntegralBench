import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the first term (3 - sqrt(5))/2
sqrt5 = mp.sqrt(5)
term1 = (3 - sqrt5) / 2

# Calculate the logarithm argument (sqrt(5) + 1)/2
log_numerator = sqrt5 + 1
log_denominator = 2
log_argument = log_numerator / log_denominator

# Calculate the second term (1/2) * ln(log_argument)
term2 = 0.5 * mp.log(log_argument)

# Combine both terms for final result
result = term1 + term2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))