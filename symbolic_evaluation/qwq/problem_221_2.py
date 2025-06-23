import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate the numerical value of 3/16
coefficient = mp.mpf(3) / 16

# Multiply by pi to get the final result
result = coefficient * mp.pi

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))