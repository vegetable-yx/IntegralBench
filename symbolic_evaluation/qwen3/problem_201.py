import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate 1 radian value using mpmath precision
angle = mp.mpf(1)

# Compute sine of 1 radian
sin_value = mp.sin(angle)

# Multiply by 2 to get final result
result = 2 * sin_value

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))