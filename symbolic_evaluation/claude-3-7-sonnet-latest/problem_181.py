import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Compute the Bessel function of the first kind of order 1.5 at 2.0
bessel_val = mp.besselj(1.5, 2.0)

# Calculate the numerator: 2 * J_{1.5}(2.0)
numerator = 2 * bessel_val

# Compute the denominator: sqrt(pi)
denominator = mp.sqrt(mp.pi)

# Evaluate the fraction: numerator / denominator
fraction = numerator / denominator

# Compute the expression inside the brackets: 1 - fraction
inner_expr = 1 - fraction

# Multiply by -pi/2
result = - (mp.pi / 2) * inner_expr

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))