import mpmath as mp

# Set internal decimal precision to 15 to ensure accurate results
mp.dps = 15

# Compute the constant pi
pi_val = mp.pi

# Compute the natural logarithm of 3
ln3_val = mp.log(3)

# Multiply pi by ln(3)
product = pi_val * ln3_val

# Divide the product by 8
result = product / 8

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))