import mpmath as mp
mp.dps = 15

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Compute numerator (sqrt(3) - 1)
numerator = sqrt3 - 1

# Calculate the argument for arcsin
arg = numerator / 2

# Compute the arcsin value
arcsin_val = mp.asin(arg)

# Multiply by 2 to get final result
result = 2 * arcsin_val

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))