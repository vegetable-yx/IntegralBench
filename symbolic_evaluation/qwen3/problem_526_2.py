import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Multiply by the logarithm result and divide by 4
result = (mp.pi * ln3) / 4

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))