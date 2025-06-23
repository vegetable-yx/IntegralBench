import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate pi divided by 4
result = mp.pi / 4

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))