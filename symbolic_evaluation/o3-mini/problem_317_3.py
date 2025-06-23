import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Define frequently used constant sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute arguments for polylog terms
arg1 = 1 - sqrt2  # Argument for first dilogarithm
arg2 = -1 - sqrt2  # Argument for second dilogarithm

# Calculate dilogarithm terms
term1 = mp.polylog(2, arg1)  # Li₂(1 - √2)
term2 = mp.polylog(2, arg2)  # Li₂(-1 - √2)

# Compute logarithms for the logarithmic product term
log_arg1 = (1 + sqrt2) / 2  # (1 + √2)/2
log_arg2 = (1 + sqrt2) / (sqrt2 - 1)  # (1 + √2)/(√2 - 1)

log_term1 = mp.log(log_arg1)  # ln((1 + √2)/2)
log_term2 = mp.log(log_arg2)  # ln((1 + √2)/(√2 - 1))

# Combine logarithmic terms
term3 = log_term1 * log_term2

# Combine all terms inside brackets: Li₂(1-√2) - Li₂(-1-√2) + log_product
inner_expr = term1 - term2 + term3

# Multiply by -√2 for final result
result = -sqrt2 * inner_expr

# Print result to 10 decimal places
print(mp.nstr(result, n=10))