import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Compute the constant pi
pi_val = mp.pi

# Compute the natural logarithm of 3
ln3_val = mp.log(3)

# Multiply pi by ln(3) and then divide by 4
result = (pi_val * ln3_val) / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))