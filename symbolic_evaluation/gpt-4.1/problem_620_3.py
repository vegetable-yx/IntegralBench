import mpmath as mp

# Set the internal decimal precision to 15 digits for intermediate calculations
mp.dps = 15

# Calculate the constant pi
pi_val = mp.pi

# Calculate the natural logarithm of 2
ln2_val = mp.log(2)

# Multiply pi by ln(2)
product = pi_val * ln2_val

# Divide the product by 8 to get the result
result = product / 8

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))