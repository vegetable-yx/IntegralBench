import mpmath as mp
mp.dps = 15  # Set precision to 15 decimal places for calculations

# Calculate the numerator
numerator = mp.mpf(4)

# Get the constant pi from mpmath
denominator = mp.pi

# Compute the division of 4 by pi
result = numerator / denominator

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))