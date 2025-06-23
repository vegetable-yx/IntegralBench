import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π^4 using mpmath's pi constant
pi_power_4 = mp.pi ** 4

# Divide by 480 to get the final result
result = pi_power_4 / 480

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))