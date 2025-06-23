import mpmath as mp
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate the logarithmic term (1 + sqrt(2))/2
log_argument = (1 + sqrt2) / 2

# Compute natural logarithm of the argument
log_term = mp.log(log_argument)

# Combine components: sqrt(2) - 1 - log_term
combined_terms = sqrt2 - 1 - log_term

# Multiply by pi/2 for final result
result = (mp.pi / 2) * combined_terms

print(mp.nstr(result, n=10))