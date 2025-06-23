import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Calculate 2 + sqrt(3)
term_2_plus_sqrt3 = 2 + sqrt3

# Compute natural logarithms of both terms
log_term1 = mp.log(term_2_plus_sqrt3)
log_term2 = mp.log(sqrt3)

# Calculate the final result by subtracting the logarithms
result = log_term1 - log_term2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))