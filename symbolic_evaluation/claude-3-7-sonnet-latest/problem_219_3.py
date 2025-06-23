import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate sin(1) in radians
sin_val = mp.sin(1)

# Multiply by 4 to get the final result
result = 4 * sin_val

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))