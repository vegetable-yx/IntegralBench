import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Convert the angle to an mpmath floating-point number
angle = mp.mpf(1)

# Compute the sine of the angle
result = mp.sin(angle)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))