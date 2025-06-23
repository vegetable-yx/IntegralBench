import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# The analytical result is exactly 1
result = mp.mpf(1)  # Convert integer 1 to mpmath floating point

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))