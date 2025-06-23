import mpmath as mp
mp.dps = 15  # Set internal precision

# Compute pi using mpmath's constant
pi_val = mp.pi

# Calculate pi^4
pi_power_4 = pi_val**4

# Divide by 120 to get the final result
result = pi_power_4 / 120

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))