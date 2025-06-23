import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute sqrt(3)
sqrt3 = mp.sqrt(3)

# Calculate numerator (sqrt(3) - 1)
numerator = sqrt3 - 1

# Compute the argument for arcsin
arg = numerator / 2

# Calculate the arcsin value
angle = mp.asin(arg)

# Multiply by 2 to get the final result
result = 2 * angle

# Print result with 10 decimal places
print(mp.nstr(result, n=10))