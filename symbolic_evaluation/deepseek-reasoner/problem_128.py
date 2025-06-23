import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate 2 times pi using mpmath constant
result = 2 * mp.pi

# Print result with 10 decimal places using nstr
print(mp.nstr(result, n=10))