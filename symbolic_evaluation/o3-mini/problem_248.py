import mpmath as mp

# Set decimal places for internal computation
mp.dps = 15

# Compute inner square root expression: sqrt(5 + 2*sqrt(5))
inner_sqrt = mp.sqrt(5 + 2 * mp.sqrt(5))

# Calculate the argument for the logarithm: (3 + inner_sqrt) / (3 - inner_sqrt)
log_arg = (3 + inner_sqrt) / (3 - inner_sqrt)

# Compute the logarithmic term: (pi/8) * ln(log_arg)
log_term = (mp.pi / 8) * mp.log(log_arg)

# Compute the argument for the dilogarithm: (inner_sqrt - 3) / (2 * inner_sqrt)
dilog_arg = (inner_sqrt - 3) / (2 * inner_sqrt)

# Compute the dilogarithm difference: Li2(dilog_arg) - Li2(-dilog_arg)
dilog_diff = mp.polylog(2, dilog_arg) - mp.polylog(2, -dilog_arg)

# Compute the dilogarithm term: (1/4) * dilog_diff
dilog_term = (1/4) * dilog_diff

# Sum both terms to get the final result
result = log_term + dilog_term

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))