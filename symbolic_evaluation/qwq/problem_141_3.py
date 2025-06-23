import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π/2 using mpmath's constant for pi
result = mp.pi / 2

# Print result with 10 decimal places using mpmath's number string function
print(mp.nstr(result, n=10))