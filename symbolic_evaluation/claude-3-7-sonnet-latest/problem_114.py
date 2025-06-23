import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute the constant pi
pi_val = mp.pi

# Compute the natural logarithm of 2
ln2_val = mp.log(2)

# Multiply pi and ln(2)
numerator = pi_val * ln2_val

# Divide the numerator by 8 to get the final result
result = numerator / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))