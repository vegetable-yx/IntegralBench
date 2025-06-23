import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate the constant pi
pi_val = mp.pi

# Calculate the square root of 3
sqrt3_val = mp.sqrt(3)

# Calculate the natural logarithm of 3
ln3_val = mp.log(3)

# Multiply pi, sqrt(3), and ln(3)
product_val = pi_val * sqrt3_val * ln3_val

# Divide the product by 36 to get the result
result = product_val / 36

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))