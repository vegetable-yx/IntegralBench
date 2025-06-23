import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Compute first term inside natural log
term_inside_first_log = 2 + sqrt3

# Calculate both logarithmic terms
log_first_term = mp.log(term_inside_first_log)
log_second_term = mp.log(sqrt3)

# Compute final result by subtracting log terms
result = log_first_term - log_second_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))