import mpmath as mp
mp.dps = 15

# Set the angle in radians
angle = mp.mpf(1)

# Calculate sine of the angle using mpmath
sin_value = mp.sin(angle)

# Store final result
result = sin_value

# Print with 10 decimal precision
print(mp.nstr(result, n=10))