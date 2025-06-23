import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate each component of the expression separately
log_term = mp.log(4/3)  # Compute ln(4/3)
multiplied_log = 3 * log_term  # Multiply by 3
dilog_term = mp.polylog(2, 1/4)  # Compute dilogarithm Li_2(1/4)

# Combine components and subtract 1
combined_terms = multiplied_log + dilog_term - 1

# Multiply by π/4 for final result
result = (mp.pi / 4) * combined_terms

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))