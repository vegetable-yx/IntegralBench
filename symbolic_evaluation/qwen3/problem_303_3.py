import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π/16
pi_over_16 = mp.pi / mp.mpf(16)

# Calculate 1/8
one_eighth = mp.mpf(1)/8

# Compute the term in parentheses (π/16 - 1/8)
parentheses_term = pi_over_16 - one_eighth

# Calculate arcsin(1/4) using mpmath's asin function
arcsin_value = mp.asin(mp.mpf(1)/4)

# Multiply the terms to get final result
result = parentheses_term * arcsin_value

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))