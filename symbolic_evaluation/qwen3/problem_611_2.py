import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sqrt(3)
sqrt3 = mp.sqrt(3)

# Compute 2 + sqrt(3)
term1 = 2 + sqrt3

# Calculate natural logarithm of (2 + sqrt(3))
log_term1 = mp.log(term1)

# Calculate natural logarithm of sqrt(3)
log_sqrt3 = mp.log(sqrt3)

# Compute final result by subtracting the logarithms
result = log_term1 - log_sqrt3

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))