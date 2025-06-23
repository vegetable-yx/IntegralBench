import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the components of the expression step by step
sqrt2 = mp.sqrt(2)  # Calculate square root of 2

# Compute the logarithm term: ln((3 + 2*sqrt2)/4)
log_numerator = 3 + 2 * sqrt2
log_arg = log_numerator / 4
log_term = mp.log(log_arg)

# Compute the fractional term: (4*sqrt2 - 5)/6
fraction_numerator = 4 * sqrt2 - 5
fraction_term = fraction_numerator / 6

# Combine terms and multiply by pi/12
combined_terms = log_term + fraction_term
result = (mp.pi / 12) * combined_terms

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))