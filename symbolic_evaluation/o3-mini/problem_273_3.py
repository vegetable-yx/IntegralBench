import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define common constants and expressions
sqrt2 = mp.sqrt(2)
log_arg = (sqrt2 + 1) / 2  # Argument for the logarithm terms

# Compute the logarithmic terms
log_val = mp.log(log_arg)
log_sq = log_val ** 2

# Compute term1: pi^3 / 96
term1 = mp.pi ** 3 / 96

# Compute term2: (pi/48) * [ln((sqrt2+1)/2)]^2
term2 = (mp.pi / 48) * log_sq

# Compute term3: -(pi/16) * ln((sqrt2+1)/2)
term3 = -(mp.pi / 16) * log_val

# Compute the arguments for the dilogarithm terms
dilog_arg1 = 1 - sqrt2/2  # 1 - sqrt(2)/2
dilog_arg2 = sqrt2/2 - 1  # sqrt(2)/2 - 1 (negative)

# Compute the dilogarithm difference: Li2(dilog_arg1) - Li2(dilog_arg2)
dilog_diff = mp.polylog(2, dilog_arg1) - mp.polylog(2, dilog_arg2)

# Compute term4: (1/24) * [Li2(dilog_arg1) - Li2(dilog_arg2)]
term4 = (1/24) * dilog_diff

# Sum all terms to get the result
result = term1 + term2 + term3 + term4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))