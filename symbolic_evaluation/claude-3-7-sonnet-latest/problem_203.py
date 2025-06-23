import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sin(1) in radians
sin_val = mp.sin(1)

# Multiply the sine result by 2
result = 2 * sin_val

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))