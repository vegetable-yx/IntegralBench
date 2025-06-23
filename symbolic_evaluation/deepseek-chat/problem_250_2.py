import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate square root of 2
sqrt_val = mp.sqrt(2)

# Subtract 1 from the square root of 2
diff_val = sqrt_val - 1

# Multiply the result by pi
result = mp.pi * diff_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))