import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the natural logarithm of 3
ln3 = mp.log(3)

# Access the constant π
pi_val = mp.pi

# Compute the numerator: ln(3) + π
numerator = ln3 + pi_val

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the denominator: 2 * √2
denominator = 2 * sqrt2

# Divide numerator by denominator to get the result
result = numerator / denominator

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))