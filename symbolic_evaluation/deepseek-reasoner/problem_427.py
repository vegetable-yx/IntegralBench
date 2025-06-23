import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the simple fraction 21/4 using high-precision arithmetic
result = mp.mpf(21) / mp.mpf(4)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))