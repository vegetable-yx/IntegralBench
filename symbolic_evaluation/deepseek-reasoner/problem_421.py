import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate sin(1) using mpmath's sin function
angle = mp.mpf(1)  # Convert input to mpmath floating-point number
result = mp.sin(angle)  # Compute sine of the angle

print(mp.nstr(result, n=10))  # Print result with 10 decimal places