import mpmath as mp

# Set internal decimal precision to 15 digits for intermediate calculations
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by pi
result = sqrt2 * mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))