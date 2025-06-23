import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute the argument for the logarithm: 3 + 2√2
log_arg = 3 + 2 * sqrt2

# Evaluate the natural logarithm: ln(3 + 2√2)
log_val = mp.log(log_arg)

# Compute the constant term: -1/(6√2)
term1 = -1 / (6 * sqrt2)

# Compute the constant term: +1/9
term2 = mp.mpf(1) / 9

# Sum all components: ln(3+2√2) - 1/(6√2) + 1/9
result = log_val + term1 + term2

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))