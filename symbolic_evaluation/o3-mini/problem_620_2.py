import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate pi constant
pi_val = mp.pi

# Calculate natural logarithm of 2
ln2_val = mp.log(2)

# Multiply pi and ln(2)
product = pi_val * ln2_val

# Divide the product by 8 to get the final result
result = product / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))