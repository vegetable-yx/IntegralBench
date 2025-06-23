import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the modified Bessel function of the first kind of order 0 at 1
i0_value = mp.besseli(0, 1)

# Multiply by pi constant
result = mp.pi * i0_value

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))