import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate 3 times pi using high-precision constant
result = 3 * mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))