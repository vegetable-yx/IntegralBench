import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate pi^4 using mpmath's constant
pi_power_4 = mp.pi**4

# Divide by 120 to get the final result
result = pi_power_4 / 120

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))