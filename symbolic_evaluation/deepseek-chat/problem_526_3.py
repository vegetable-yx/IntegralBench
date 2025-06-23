import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate pi (π) and natural logarithm of 3 (ln(3))
pi_value = mp.pi
ln3_value = mp.log(3)

# Multiply π by ln(3)
product = pi_value * ln3_value

# Divide the product by 4 to get the final result
result = product / 4

# Output the result with exactly 10 decimal places
print(mp.nstr(result, n=10))