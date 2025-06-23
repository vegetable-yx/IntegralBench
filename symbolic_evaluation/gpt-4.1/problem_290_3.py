import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute the final result by dividing pi by 8
result = pi_value / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))