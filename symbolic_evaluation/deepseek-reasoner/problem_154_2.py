import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate sqrt(2) - 1
s = mp.sqrt(2) - 1

# Compute natural logarithm of (sqrt(2) - 1)
ln_term = mp.log(s)

# Calculate dilogarithm terms
Li2_s = mp.polylog(2, s)
Li2_1ms = mp.polylog(2, 1 - mp.sqrt(2))
sum_Li2 = Li2_s + Li2_1ms

# Calculate trilogarithm terms
Li3_s = mp.polylog(3, s)
Li3_1ms = mp.polylog(3, 1 - mp.sqrt(2))

# Combine all components
combined_term = ln_term * sum_Li2 - Li3_s + Li3_1ms
result = 0.5 * combined_term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))