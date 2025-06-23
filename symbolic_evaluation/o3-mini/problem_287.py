import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute constants
sqrt2 = mp.sqrt(2)
a = 1 + sqrt2  # Argument for the first logarithm
b = a / 2      # Argument for the second logarithm (i.e., (1+sqrt2)/2)

# Calculate logarithmic terms
log_a = mp.log(a)
log_b = mp.log(b)

# Compute squared logarithms
log_a_sq = log_a ** 2
log_b_sq = log_b ** 2

# Calculate polylog terms
polylog_neg = mp.polylog(2, -1/sqrt2)  # Li_2(-1/sqrt(2))
polylog_pos = mp.polylog(2, 1/sqrt2)   # Li_2(1/sqrt(2))

# Compute each term of the expression
term1 = (mp.pi / 8) * log_a_sq
term2 = (1/16) * log_b_sq
term3 = (1/8) * polylog_neg
term4 = (1/8) * polylog_pos

# Combine terms: term1 - term2 - term3 + term4
result = term1 - term2 - term3 + term4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))