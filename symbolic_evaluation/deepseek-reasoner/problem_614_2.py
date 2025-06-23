import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the simple fraction 1/2 using high-precision arithmetic
result = mp.mpf(1)/2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))