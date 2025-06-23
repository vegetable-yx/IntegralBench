import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the fraction 5/3 with mpmath precision
fraction = mp.mpf(5)/mp.mpf(3)

# Compute natural logarithm of 5/3
log_result = mp.log(fraction)

# Divide the logarithm result by 8
term1 = log_result / mp.mpf(8)

# Calculate 1/20 with mpmath precision
term2 = mp.mpf(1)/mp.mpf(20)

# Combine terms for final result
result = term1 - term2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))