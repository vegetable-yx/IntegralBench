import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sin(2) and cos(2)
sin_2 = mp.sin(2)
cos_2 = mp.cos(2)

# Compute the numerator components
two_cos2 = 2 * cos_2
numerator_part = sin_2 - two_cos2

# Square the numerator component
numerator_squared = numerator_part ** 2

# Final result calculation
result = numerator_squared / 32

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))