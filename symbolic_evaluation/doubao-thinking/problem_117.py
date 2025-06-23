import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Compute π raised to the fourth power
pi_power4 = pi_value**4

# Divide the result by 128 to get the final value
result = pi_power4 / 128

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))