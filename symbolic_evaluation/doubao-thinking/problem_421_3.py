import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Define the angle in radians (1 radian)
angle = mp.mpf(1)

# Compute sine of the angle
result = mp.sin(angle)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))