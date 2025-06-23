import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the coefficient 3/4
coefficient = mp.mpf(3)/4

# Multiply by pi constant from mpmath
result = coefficient * mp.pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))