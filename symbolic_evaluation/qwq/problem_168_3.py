import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Compute π cubed
pi_cubed = mp.power(pi_value, 3)

# Divide by 8 to get final result
result = mp.fdiv(pi_cubed, 8)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))