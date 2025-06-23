import mpmath as mp
mp.dps = 15

# Calculate the coefficient
coefficient = 506

# Multiply by pi using high-precision constant
result = coefficient * mp.pi

# Print result with 10 decimal places
print(mp.nstr(result, n=10))