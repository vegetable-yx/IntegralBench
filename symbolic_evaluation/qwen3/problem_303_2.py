import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate arcsin(1/4) using mpmath's asin function
arcsin_val = mp.asin(mp.mpf(1)/4)

# Square the arcsin result
arcsin_squared = arcsin_val ** 2

# Multiply by pi and divide by 32
result = (mp.pi * arcsin_squared) / 32

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))