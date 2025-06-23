import mpmath as mp
mp.dps = 15

# Calculate -3π directly using mpmath's pi constant
result = -3 * mp.pi

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))