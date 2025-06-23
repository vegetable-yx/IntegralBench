import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi
pi_val = mp.pi

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Multiply pi and ln3
pi_ln3 = pi_val * ln3

# Divide by 8 and negate the result
result = -pi_ln3 / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))