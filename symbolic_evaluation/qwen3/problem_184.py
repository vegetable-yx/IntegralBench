import mpmath as mp
mp.dps = 15

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Multiply π with the calculated logarithm
pi_ln3_product = mp.pi * ln3

# Divide the product by 8 to get final result
result = pi_ln3_product / 8

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))