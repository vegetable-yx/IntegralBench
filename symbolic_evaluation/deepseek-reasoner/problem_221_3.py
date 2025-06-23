import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate 3/16 fraction using arbitrary precision
coefficient = mp.mpf(3) / mp.mpf(16)

# Multiply by pi using mpmath's constant
result = coefficient * mp.pi

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))