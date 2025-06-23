import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute the final result as pi divided by 2
result = pi_value / 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))