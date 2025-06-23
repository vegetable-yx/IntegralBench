import mpmath as mp
mp.dps = 15  # Set decimal precision for intermediate calculations

# Calculate sin(2) using mpmath
sin_2 = mp.sin(2)

# Compute the sine term component (sin(2)/2)
sine_component = sin_2 / 2

# Calculate sqrt(2) using mpmath
sqrt2 = mp.sqrt(2)

# Compute the coefficient (sqrt(2)/pi)
coefficient = sqrt2 / mp.pi

# Combine components to get final result
result = coefficient * sine_component

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))