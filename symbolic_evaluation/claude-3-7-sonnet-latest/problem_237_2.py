import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate the square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply by 4 and by pi
result = 4 * mp.pi * sqrt_2

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))