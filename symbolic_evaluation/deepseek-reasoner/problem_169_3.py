import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π²/3 term
pi_squared_over_3 = mp.pi**2 / 3

# Calculate 2π√3 term
two_pi_sqrt3 = 2 * mp.pi * mp.sqrt(3)

# Calculate -4π term
minus_four_pi = -4 * mp.pi

# Combine all components
result = pi_squared_over_3 + two_pi_sqrt3 + minus_four_pi

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))