import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the angle in radians
angle = mp.mpf(1)

# Compute sine of the angle using mpmath's sin function
result = mp.sin(angle)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))