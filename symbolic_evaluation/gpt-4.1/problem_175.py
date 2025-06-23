import mpmath as mp

# Set precision to 15 decimal places
mp.dps = 15

# Compute the dilogarithm term: Li_2(1/4)
dilog_term = mp.polylog(2, mp.mpf(1)/4)

# Compute the natural logarithm term: ln(3/4)
log_term = mp.log(mp.mpf(3)/4)

# Combine the terms: Li_2(1/4) + 3 * ln(3/4) + 1
inner_expr = dilog_term + 3 * log_term + 1

# Multiply by pi/4 to get the result
result = (mp.pi / 4) * inner_expr

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))