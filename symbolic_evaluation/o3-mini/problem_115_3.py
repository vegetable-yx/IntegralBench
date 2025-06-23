import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Arguments for the dilogarithm functions
arg1 = 1 + 1/sqrt2
arg2 = 1 - 1/sqrt2

# Compute the difference of dilogarithms
dilog_diff = mp.polylog(2, arg1) - mp.polylog(2, arg2)

# Multiply by sqrt(2)/8
term1 = (sqrt2 / 8) * dilog_diff

# Compute the argument for the logarithm
log_arg = (sqrt2 + 1) / (sqrt2 - 1)

# Compute the logarithmic term: (1/4) * ln(log_arg)
term2 = (1/4) * mp.log(log_arg)

# Compute the constant term: -pi/8
term3 = -mp.pi / 8

# Sum all terms
result = term1 + term2 + term3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))