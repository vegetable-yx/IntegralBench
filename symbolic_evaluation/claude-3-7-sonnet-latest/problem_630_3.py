import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate common constants and expressions
pi = mp.pi
sqrt3 = mp.sqrt(3)

# Precompute the logarithm argument
numerator = 3 + sqrt3
denominator = 1 + sqrt3
log_arg = numerator / denominator

# Compute the two main terms
term1 = (pi / (3 * sqrt3)) * mp.log(3)
term2 = (pi / (2 * sqrt3)) * mp.log(log_arg)

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))