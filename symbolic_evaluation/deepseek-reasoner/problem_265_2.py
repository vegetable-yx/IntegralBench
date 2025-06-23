import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Compute Bessel functions of the first kind
J0_2 = mp.besselj(0, 2)
J1_2 = mp.besselj(1, 2)

# Compute Struve H functions
H0_2 = mp.struveh(0, 2)
H1_2 = mp.struveh(1, 2)

# Calculate the main bracket component
bracket_component = J0_2 * H1_2 - J1_2 * H0_2

# Multiply by pi/8
pi_term = (mp.pi / 8) * bracket_component

# Compute the sine term component
sin_term = mp.sin(2) / 4

# Combine all components for final result
result = pi_term - sin_term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))