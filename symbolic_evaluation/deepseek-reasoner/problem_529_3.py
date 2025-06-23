import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the negative value of pi
result = -mp.pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))