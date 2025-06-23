import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate 2 * pi using mpmath constant
result = 2 * mp.pi

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))