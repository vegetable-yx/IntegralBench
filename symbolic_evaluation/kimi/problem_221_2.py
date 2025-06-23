import mpmath as mp

mp.dps = 15  # Set decimal places for internal calculations

# Calculate the coefficient -61/16 using high-precision division
coefficient = mp.mpf(-61) / 16

# Multiply coefficient by pi to get the final result
result = coefficient * mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))