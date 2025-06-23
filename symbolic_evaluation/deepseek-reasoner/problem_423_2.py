import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Assign the exact integer value from analytical solution
result = mp.mpf(99)

# Print result with 10 decimal place formatting
print(mp.nstr(result, n=10))