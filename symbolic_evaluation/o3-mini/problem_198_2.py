import mpmath as mp

# Set the decimal places for internal precision
mp.dps = 15

# Define the argument for Bessel functions
x_val = mp.mpf('0.5')

# Calculate each Bessel function separately
# J_{-1/4}(1/2)
j_minus_14 = mp.besselj(-0.25, x_val)

# J_{3/4}(1/2)
j_34 = mp.besselj(0.75, x_val)

# J_{1/4}(1/2)
j_14 = mp.besselj(0.25, x_val)

# J_{-3/4}(1/2)
j_minus_34 = mp.besselj(-0.75, x_val)

# Compute the sum of products: J_{-1/4} * J_{3/4} + J_{1/4} * J_{-3/4}
sum_products = j_minus_14 * j_34 + j_14 * j_minus_34

# Multiply by pi/sqrt(2)
result = (mp.pi / mp.sqrt(2)) * sum_products

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))