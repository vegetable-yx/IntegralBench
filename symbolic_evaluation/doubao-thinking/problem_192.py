import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate components for the first term
sqrt2 = mp.sqrt(2)
log_arg = (1 + sqrt2) / 2
log_sq_term = mp.log(log_arg) ** 2
part_a = mp.pi/4 * log_sq_term

# Calculate dilogarithm component
dilog_arg = (1 - sqrt2) / 2
part_b = mp.pi/2 * mp.polylog(2, dilog_arg)

# Calculate linear combination components
linear_comb = sqrt2 - mp.log(1 + sqrt2) - 1 + mp.log(2)
part_c = mp.pi * linear_comb

# Combine all parts
result = part_a + part_b + part_c

# Print final result with 10 decimal precision
print(mp.nstr(result, n=10))