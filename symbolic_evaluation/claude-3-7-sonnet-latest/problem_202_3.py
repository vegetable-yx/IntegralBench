import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the angle in radians
angle = mp.mpf('1.0')

# Calculate sine of the angle
sin_val = mp.sin(angle)

# Multiply by 4.0
scaled_sin = mp.mpf('4.0') * sin_val

# Add the constant term
result = mp.mpf('-4.0') + scaled_sin

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))