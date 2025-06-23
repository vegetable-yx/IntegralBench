import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate pi using mpmath's built-in constant
pi_value = mp.pi

# Compute the result as pi divided by 4
result = pi_value / 4

# Print the final result with 10 decimal places precision
print(mp.nstr(result, n=10))