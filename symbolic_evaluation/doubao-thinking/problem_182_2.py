import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the natural logarithm term: ln(2 + sqrt(5))
sqrt5 = mp.sqrt(5)  # Compute square root of 5
inner_log = 2 + sqrt5  # Compute 2 + sqrt(5)
log_term = mp.log(inner_log)  # Natural logarithm of (2 + sqrt(5))

# Compute the fraction: (sqrt(5) - 1) / 2
fraction = (sqrt5 - 1) / 2

# Combine the terms: log_term - fraction
combined = log_term - fraction

# Multiply by pi to get the final result
result = mp.pi * combined

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))