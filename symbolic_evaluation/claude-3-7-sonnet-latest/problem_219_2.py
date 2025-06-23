import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate sin(1) and store in a variable
sin_val = mp.sin(1)

# Calculate cos(1) and store in a variable
cos_val = mp.cos(1)

# Compute the expression: -32 * sin(1) - 24 * cos(1) + 48
result = -32 * sin_val - 24 * cos_val + 48

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))