import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 1 + sqrt(2)
sqrt_2 = mp.sqrt(2)
sum_term = 1 + sqrt_2

# Calculate natural logarithm of (1 + sqrt(2))
log_term = mp.log(sum_term)

# Calculate pi/4
pi_quarter = mp.pi / 4

# Multiply components to get final result
result = pi_quarter * log_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))