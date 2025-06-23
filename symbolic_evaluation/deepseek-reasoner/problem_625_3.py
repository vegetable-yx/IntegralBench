import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π (pi) using mpmath's constant
pi_value = mp.pi

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply π by sqrt(2)
product = pi_value * sqrt2

# Divide the product by 4 to get final result
result = product / 4

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))