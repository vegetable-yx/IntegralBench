import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute constants: sqrt(2) and (1 + sqrt(2))
sqrt2 = mp.sqrt(2)
sqrt2_minus_1 = sqrt2 - 1
one_minus_sqrt2 = 1 - sqrt2
one_plus_sqrt2 = 1 + sqrt2

# Calculate the two dilogarithm terms
dilog1 = mp.polylog(2, sqrt2_minus_1)  # Li_2(√2 - 1)
dilog2 = mp.polylog(2, one_minus_sqrt2)  # Li_2(1 - √2)

# Compute the dilogarithm part: (1/2)[Li_2(√2-1) - Li_2(1-√2)]
dilog_part = 0.5 * (dilog1 - dilog2)

# Compute the logarithmic part: (π/4) * ln(1 + √2)
log_term = mp.log(one_plus_sqrt2)
log_part = (mp.pi / 4) * log_term

# Sum both parts to get the final result
result = dilog_part + log_part

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))