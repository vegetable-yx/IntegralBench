import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the argument for the logarithm: (sqrt(6) + 1)/(sqrt(6) - 1)
sqrt6 = mp.sqrt(6)
log_arg = (sqrt6 + 1) / (sqrt6 - 1)

# Compute the first term: (pi/8) * ln(log_arg)
term1 = (mp.pi / 8) * mp.log(log_arg)

# Compute arguments for the dilogarithm functions
sqrt5 = mp.sqrt(5)
arg1 = (sqrt5 + 1) / 2  # (sqrt(5) + 1)/2
arg2 = (sqrt5 - 1) / 2  # (sqrt(5) - 1)/2

# Compute the difference of dilogarithms: Li2(arg1) - Li2(arg2)
dilog_diff = mp.polylog(2, arg1) - mp.polylog(2, arg2)

# Compute the second term: (1/8) * dilog_diff
term2 = (1/8) * dilog_diff

# Sum the two terms
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))