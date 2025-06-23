import mpmath as mp
mp.dps = 15  # Set decimal precision for internal calculations

# Calculate sin(1) using mpmath's sin function
angle = mp.mpf(1)  # Convert 1 to mpmath floating-point
result = mp.sin(angle)  # Compute sine of 1 radian

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))