import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate components of the expression step by step
sqrt5 = mp.sqrt(5)          # Compute square root of 5
two_plus_sqrt5 = 2 + sqrt5    # Calculate (2 + √5)
log_term = mp.log(two_plus_sqrt5)  # Compute logarithm of (2 + √5)
pi_over_4 = mp.pi / 4         # Precompute π/4 coefficient

# Combine components to get final result
result = pi_over_4 * log_term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))