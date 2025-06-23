import mpmath as mp

mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute argument for dilogarithm function
dilog_argument = (sqrt2 - 1) / 2

# Calculate dilogarithm term
li2_term = mp.polylog(2, dilog_argument)

# Compute argument for logarithmic term
log_argument = (sqrt2 + 1) / 2

# Calculate squared logarithm term
log_term = mp.log(log_argument)
log_squared = log_term ** 2

# Combine components to form final expression
combined_terms = 2 * li2_term - log_squared
result = sqrt2 * mp.pi * combined_terms

print(mp.nstr(result, n=10))