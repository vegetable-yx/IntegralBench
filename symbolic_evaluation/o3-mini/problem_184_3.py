import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the constant pi
pi_val = mp.pi

# Calculate the natural logarithm of 3
ln3_val = mp.log(3)

# Multiply pi and ln(3) to form the numerator
numerator = pi_val * ln3_val

# Divide the numerator by 8 to obtain the final result
result = numerator / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))