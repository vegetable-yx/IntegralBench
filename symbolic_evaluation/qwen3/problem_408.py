import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 5/3 using high-precision arithmetic
fraction = mp.mpf(5)/mp.mpf(3)

# Compute natural logarithm of the fraction
log_term = mp.log(fraction)

# Calculate first term: (1/8) * ln(5/3)
term1 = log_term / mp.mpf(8)

# Calculate second term: 1/20
term2 = mp.mpf(1)/mp.mpf(20)

# Combine terms to get final result
result = term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))