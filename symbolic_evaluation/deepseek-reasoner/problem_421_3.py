import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sin(1) using mpmath's sin function
angle = mp.mpf(1)  # Convert 1 to mpmath floating-point number
result = mp.sin(angle)  # Compute sine of 1 radian

print(mp.nstr(result, n=10))