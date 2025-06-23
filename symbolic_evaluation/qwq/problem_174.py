import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate arcsin(1/4)
arcsin_term = mp.asin(mp.mpf(1)/4)

# Square the arcsin term
arcsin_squared = mp.power(arcsin_term, 2)

# Multiply by pi/4
result = (mp.pi/4) * arcsin_squared

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))