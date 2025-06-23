import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sqrt(3) and divide by 8
sqrt_term = mp.sqrt(3) / 8

# Calculate pi squared and divide by 72
pi_sq_term = mp.pi**2 / 72

# Combine terms for final result
result = sqrt_term - pi_sq_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))