import mpmath as mp

# Set decimal precision to 15 for internal calculations
mp.dps = 15

# Calculate pi using mpmath's built-in constant
pi_value = mp.pi

# Compute the result by dividing pi by 8
result = pi_value / 8

# Print the final result with 10 decimal places precision
print(mp.nstr(result, n=10))