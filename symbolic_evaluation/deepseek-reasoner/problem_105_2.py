import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Calculate pi divided by 3
pi_term = mp.pi / 3

# Combine results for final calculation
result = sqrt3 - pi_term

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))