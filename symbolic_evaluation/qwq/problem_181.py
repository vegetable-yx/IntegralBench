import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate trigonometric components
sin_2 = mp.sin(2)
cos_2 = mp.cos(2)

# Compute numerator component
numerator = sin_2 - 2 * cos_2

# Combine all components
result = (sqrt_pi * numerator) / 16

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))