import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate pi^4 by first squaring pi
pi_squared = mp.pi ** 2
pi_fourth = pi_squared ** 2  # Square again to get pi^4

# Compute the numerator (9 * pi^4)
numerator = 9 * pi_fourth

# Final calculation with denominator 256
result = numerator / 256

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))