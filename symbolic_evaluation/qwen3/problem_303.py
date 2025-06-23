import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π/16 term
pi_over_16 = mp.pi / 16

# Compute arcsin(1/4) using mpmath's asin function
arcsin_term = mp.asin(mp.mpf(1)/4)

# First term: (π/16) * arcsin(1/4)
term1 = pi_over_16 * arcsin_term

# Second term: -1/4
term2 = -mp.mpf(1)/4

# Compute natural logarithm of 5/3
log_term = mp.log(mp.mpf(5)/3)

# Third term: (15/32) * ln(5/3)
term3 = (mp.mpf(15)/32) * log_term

# Combine all terms
result = term1 + term2 + term3

# Print result with 10 decimal places using mpmath's nstr
print(mp.nstr(result, n=10))