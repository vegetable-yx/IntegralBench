import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Define the angle in radians
angle = 1

# Compute sine of the angle
result = mp.sin(angle)

# Output the result to 10 decimal places
print(mp.nstr(result, n=10))