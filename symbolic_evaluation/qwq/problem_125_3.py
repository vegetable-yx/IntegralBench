import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi^4
pi_power4 = mp.pi ** 4

# Divide by 96 to get the final result
result = pi_power4 / 96

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))