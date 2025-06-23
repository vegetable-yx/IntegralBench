import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate the product of 2019 and pi
product = 2019 * mp.pi

# Compute the square root of the product
sqrt_product = mp.sqrt(product)

# Divide the square root by 2019 to obtain the result
result = sqrt_product / 2019

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))