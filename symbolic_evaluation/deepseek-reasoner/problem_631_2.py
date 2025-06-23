import mpmath as mp
mp.dps = 15

# Calculate the angle in radians
angle = mp.mpf(1)

# Compute sine of the angle
result = mp.sin(angle)

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))