import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Calculate the argument for the logarithm: 3 + 2*sqrt(2)
log_arg = 3 + 2 * sqrt2

# Compute the natural logarithm of the argument
log_value = mp.log(log_arg)

# Calculate the coefficient: 11/(8*sqrt(2))
coefficient = 11 / (8 * sqrt2)

# Multiply the coefficient by the logarithm
product = coefficient * log_value

# Compute the constant term: -1/2
constant_term = -0.5

# Sum the constant term and the product
result = constant_term + product

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))