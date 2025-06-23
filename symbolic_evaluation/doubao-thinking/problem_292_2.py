import mpmath as mp
mp.dps = 15  # Set decimal precision for intermediate calculations

# Calculate pi using mpmath's built-in constant
pi_value = mp.pi

# Compute pi raised to the fourth power
pi_power = pi_value ** 4

# Divide by 16 to get the final result
result = pi_power / 16

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))