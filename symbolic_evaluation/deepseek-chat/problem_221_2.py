import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Get the mathematical constant π
pi_value = mp.pi

# Multiply π by 9
numerator = 9 * pi_value

# Divide the numerator by 16 to obtain the final result
result = numerator / 16

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))