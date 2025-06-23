import mpmath as mp

# Set internal decimal places for high precision calculations
mp.dps = 15

# Define the angle in radians
angle = mp.mpf(1)

# Calculate the sine of the angle
result = mp.sin(angle)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))