import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate components separately
pi_val = mp.pi  # Get pi constant
term = 1 - (pi_val / 2)  # Compute (1 - π/2)
sqrt_two = mp.sqrt(2)  # Compute square root of 2

# Combine components for final result
result = sqrt_two * pi_val * term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))