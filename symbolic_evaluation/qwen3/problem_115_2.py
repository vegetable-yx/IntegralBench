import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate the natural logarithm term: ln(1 + sqrt(2))
log_arg = 1 + sqrt2
ln_term = mp.log(log_arg)

# Multiply components together: sqrt(2) * pi * ln_term
sqrt2_pi = sqrt2 * mp.pi
result = sqrt2_pi * ln_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))