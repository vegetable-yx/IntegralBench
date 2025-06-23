import mpmath as mp

mp.dps = 15  # Set decimal places for internal calculations

# Calculate pi^4 by squaring pi twice
pi_squared = mp.pi ** 2
pi_power4 = pi_squared ** 2

# Compute denominator
denominator = 56

# Calculate final result
result = pi_power4 / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))