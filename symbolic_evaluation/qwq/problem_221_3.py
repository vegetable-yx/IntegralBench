import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate the constant coefficient 3/16
coefficient = mp.mpf(3) / mp.mpf(16)

# Multiply by pi to get the final result
result = coefficient * mp.pi

# Print result with 10 decimal places
print(mp.nstr(result, n=10))