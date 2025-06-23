import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute each component of the expression step by step
sqrt_pi = mp.sqrt(mp.pi)  # Calculate square root of pi
sqrt_2 = mp.sqrt(2)  # Calculate square root of 2
log_term = mp.log(1 + sqrt_2)  # Compute natural logarithm term

# Combine components according to the formula
combined_terms = sqrt_2 - log_term
result = 2 * sqrt_pi * combined_terms  # Multiply by 2*sqrt(pi)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))