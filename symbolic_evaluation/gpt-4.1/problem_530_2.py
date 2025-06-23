import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the argument for the logarithm: (1 + sqrt(2))
log_arg = 1 + sqrt2

# Compute the natural logarithm of (1 + sqrt(2))
log_term = mp.log(log_arg)

# Multiply by 2*sqrt(2)
product_term = 2 * sqrt2 * log_term

# Subtract the product from 3 to get the final result
result = 3 - product_term

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))