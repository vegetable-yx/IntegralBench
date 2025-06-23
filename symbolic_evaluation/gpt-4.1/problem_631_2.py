import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the angle in radians (1 radian)
x = mp.mpf(1)

# Compute sine of the angle
result = mp.sin(x)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))