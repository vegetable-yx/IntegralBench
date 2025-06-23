import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant pi
pi_val = mp.pi

# Compute the natural logarithm of 3
ln3 = mp.log(3)

# Multiply pi and ln(3)
pi_ln3 = pi_val * ln3

# Divide by 4 to get the final result
result = pi_ln3 / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))