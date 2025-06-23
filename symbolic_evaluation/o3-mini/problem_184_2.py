import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute π using mpmath's constant
pi_val = mp.pi

# Compute natural logarithm of 3
ln3 = mp.log(3)

# Multiply π and ln(3)
product = pi_val * ln3

# Divide the product by 8
result = product / 8

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))