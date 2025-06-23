import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π/4 component
pi_term = mp.pi / 4

# Calculate sin(2) component
sin_2 = mp.sin(2)
sin_term = sin_2 / 4

# Combine terms for final result
result = pi_term - sin_term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))