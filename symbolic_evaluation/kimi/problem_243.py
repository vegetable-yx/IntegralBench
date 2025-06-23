import mpmath as mp
mp.dps = 15

# Calculate 3/8 fraction component
coefficient = mp.mpf(3)/8

# Multiply by pi constant
result = coefficient * mp.pi

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))