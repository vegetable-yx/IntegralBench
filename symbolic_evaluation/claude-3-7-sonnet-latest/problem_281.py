import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Define variables a and b (example values, user should replace with actual values)
a = 1.0
b = 1.0

# Calculate the product b*a
product_ba = b * a

# Calculate the argument for the square root: (4*pi)/(b*a)
sqrt_arg = (4 * mp.pi) / product_ba

# Compute the square root term: sqrt((4*pi)/(b*a))
sqrt_term = mp.sqrt(sqrt_arg)

# Calculate the argument for cosh: (b*a)/2
cosh_arg = product_ba / 2

# Compute the hyperbolic cosine term: cosh((b*a)/2)
cosh_term = mp.cosh(cosh_arg)

# Multiply both terms to get the final result
result = sqrt_term * cosh_term

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))