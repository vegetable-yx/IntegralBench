import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Assign Euler's number directly from mpmath constants
result = mp.e

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))