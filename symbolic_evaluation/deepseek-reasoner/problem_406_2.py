import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate the numerator part (sqrt(3) - 1)
sqrt3 = mp.sqrt(3)
numerator = sqrt3 - 1

# Calculate the argument for arcsin
asin_arg = numerator / 2

# Compute the arcsin value and multiply by 2
arcsin_value = mp.asin(asin_arg)
result = 2 * arcsin_value

# Print result with 10 decimal places
print(mp.nstr(result, n=10))