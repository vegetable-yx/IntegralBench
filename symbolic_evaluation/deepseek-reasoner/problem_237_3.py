import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate 4 times pi using exact symbolic constant
result = 4 * mp.pi

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))