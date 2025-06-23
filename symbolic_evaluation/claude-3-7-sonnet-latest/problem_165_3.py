import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sine of 2.0 radians
sin_value = mp.sin(2.0)

# Multiply by pi to get final result
result = mp.pi * sin_value

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))