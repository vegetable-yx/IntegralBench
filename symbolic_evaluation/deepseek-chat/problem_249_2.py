import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Compute the mathematical constant pi
pi_value = mp.pi

# Compute the natural logarithm of 2
ln2_value = mp.log(2)

# Multiply pi and ln(2) to get the result
result = pi_value * ln2_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))