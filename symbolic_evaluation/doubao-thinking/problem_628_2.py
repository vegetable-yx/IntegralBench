import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the numerator (π + 2)
numerator = mp.pi + 2

# Divide by 8 to get the fraction
fraction = numerator / 8

# Apply the negative sign to get final result
result = -fraction

# Print result with 10 decimal places
print(mp.nstr(result, n=10))