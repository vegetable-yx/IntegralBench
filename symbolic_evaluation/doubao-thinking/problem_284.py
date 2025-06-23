import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute 1 + sqrt(2)
one_plus_sqrt2 = 1 + sqrt2

# Compute the natural logarithm of (1 + sqrt(2))
ln_value = mp.log(one_plus_sqrt2)

# Square the logarithm
ln_squared = ln_value ** 2

# Multiply by pi and divide by 8
result = (mp.pi * ln_squared) / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))