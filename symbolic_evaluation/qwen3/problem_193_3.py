import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate pi^4
pi_squared = mp.pi ** 2
pi_power4 = pi_squared ** 2

# Divide by 48 to get final result
result = pi_power4 / 48

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))