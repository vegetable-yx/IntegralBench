import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute pi raised to the fourth power
pi_power4 = pi_value**4

# Divide the result by 256
result = pi_power4 / 256

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))