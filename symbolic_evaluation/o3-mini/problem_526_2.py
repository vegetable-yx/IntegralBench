import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate π (pi) using mpmath constant
pi_val = mp.pi

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Multiply π by ln(3)
product = pi_val * ln3

# Divide the product by 4
result = product / 4

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))