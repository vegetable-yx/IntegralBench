import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the coefficient
coefficient = mp.mpf(-3)

# Multiply by pi constant from mpmath
result = coefficient * mp.pi

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))