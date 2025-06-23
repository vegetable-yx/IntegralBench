import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the constant coefficient
coefficient = mp.mpf(19) / 512

# Multiply by π to get the final result
result = coefficient * mp.pi

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))