import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi^4
pi_power_4 = mp.pi ** 4

# Multiply by 7 to get the numerator
numerator = 7 * pi_power_4

# Divide by 24 to get the final result
result = numerator / 24

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))