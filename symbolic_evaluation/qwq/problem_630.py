import mpmath as mp

mp.dps = 15  # Set internal decimal precision

# Calculate each component separately
sqrt3 = mp.sqrt(3)  # Square root of 3
ln3 = mp.log(3)     # Natural logarithm of 3

# Multiply components following the formula structure
pi_term = mp.pi * sqrt3  # Combine π and √3
combined = pi_term * ln3  # Multiply by ln(3)
result = combined / 36    # Final division by 36

print(mp.nstr(result, n=10))