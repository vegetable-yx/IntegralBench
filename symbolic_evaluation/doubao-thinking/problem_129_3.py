import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the constant 2
two = mp.mpf(2)

# Multiply 2 by pi
product = two * mp.pi

# Take the square root of (2 * pi)
result = mp.sqrt(product)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))