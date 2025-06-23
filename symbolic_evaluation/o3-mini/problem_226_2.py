import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate constant terms: pi^3 / 16
pi = mp.pi
term1 = mp.power(pi, 3) / 16

# Compute the logarithm argument: (1 + sqrt(2)) / 2
sqrt2 = mp.sqrt(2)
log_arg = (1 + sqrt2) / 2

# Calculate the squared natural logarithm: ln^2((1+sqrt(2))/2)
log_val = mp.log(log_arg)
log_sq = mp.power(log_val, 2)
term2 = (pi / 4) * log_sq

# Compute arguments for dilogarithms
dilog_arg1 = 1 - sqrt2/2  # 1 - sqrt(2)/2
dilog_arg2 = 1 + sqrt2/2  # 1 + sqrt(2)/2

# Calculate dilogarithms: Li_2(1 - sqrt(2)/2) and Li_2(1 + sqrt(2)/2)
dilog1 = mp.polylog(2, dilog_arg1)
dilog2 = mp.polylog(2, dilog_arg2)

# Combine dilogarithm terms: (1/2)*dilog1 - (1/2)*dilog2
term3 = 0.5 * dilog1
term4 = -0.5 * dilog2

# Sum all terms to get final result
result = term1 + term2 + term3 + term4

# Print result to 10 decimal places
print(mp.nstr(result, n=10))