import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Square the logarithm value
ln2_squared = ln2 ** 2

# Divide by 2 to get final result
result = ln2_squared / 2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))