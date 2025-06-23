import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi^4
pi_power_4 = mp.pi**4

# Multiply by 7
numerator = 7 * pi_power_4

# Divide by 240 to get final result
result = numerator / 240

# Print result with 10 decimal places
print(mp.nstr(result, n=10))