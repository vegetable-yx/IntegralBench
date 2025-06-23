import mpmath as mp

# Set internal precision to 15 decimal places for accuracy
mp.dps = 15

# Compute the constant π
pi_val = mp.pi

# Compute the natural logarithm of 3
ln3_val = mp.log(3)

# Multiply π and ln(3)
product_val = pi_val * ln3_val

# Divide the product by 4
result = product_val / 4

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))