import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant factor 7/240
constant = mp.mpf(7) / mp.mpf(240)

# Calculate pi^4
pi_power_4 = mp.pi ** 4

# Compute the entire expression: (7/240) * pi^4
result = constant * pi_power_4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))