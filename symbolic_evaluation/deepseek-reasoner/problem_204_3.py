import mpmath as mp
mp.dps = 15

# Calculate exponential term e^(-1/4)
exp_term = mp.exp(-mp.mpf(1)/4)

# Calculate 6 times the exponential term
six_exp = 6 * exp_term

# Compute numerator part (5 - 6e^{-1/4})
numerator = 5 - six_exp

# Calculate sqrt(2)/16 coefficient
sqrt2_div_16 = mp.sqrt(2) / 16

# Combine components for final result
result = sqrt2_div_16 * numerator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))