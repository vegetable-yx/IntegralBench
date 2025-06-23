import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the argument for the logarithm
sqrt2 = mp.sqrt(2)
log_arg = (1 + sqrt2)**2 / 2

# Compute the logarithmic term: pi * ln(log_arg)
log_term = mp.pi * mp.log(log_arg)

# Compute the dilogarithm terms
dilog_term1 = mp.polylog(2, 1 - sqrt2)  # Li_2(1 - sqrt(2))
dilog_term2 = mp.polylog(2, sqrt2 - 1)  # Li_2(sqrt(2) - 1)

# Combine all terms inside the brackets
bracket_term = log_term + dilog_term1 - dilog_term2

# Multiply by 1/32
result = bracket_term / 32

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))