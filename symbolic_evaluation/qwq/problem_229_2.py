import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate pi using mpmath's built-in constant
pi_value = mp.pi

# Compute pi to the fourth power
pi_fourth_power = pi_value**4

# Divide by 15 to get the final result
result = pi_fourth_power / 15

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))