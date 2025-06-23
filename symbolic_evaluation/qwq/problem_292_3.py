import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi^4
pi_power_4 = mp.pi ** 4

# Divide by 24 to get the final result
result = pi_power_4 / 24

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))