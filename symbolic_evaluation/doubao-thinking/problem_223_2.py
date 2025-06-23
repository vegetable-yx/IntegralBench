import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate Catalan's constant component
catalan_term = 8 * mp.catalan

# Calculate pi squared component
pi_squared_term = (mp.pi ** 2) / 2

# Combine terms for final result
result = catalan_term - pi_squared_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))