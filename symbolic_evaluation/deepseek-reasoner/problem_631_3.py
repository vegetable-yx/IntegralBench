import mpmath as mp

# Set decimal places of precision for internal calculations
mp.dps = 15

# Calculate the angle in radians
angle = mp.mpf(1)

# Compute the sine of the angle
result = mp.sin(angle)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))