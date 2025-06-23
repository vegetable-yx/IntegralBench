import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Define the parameter 'a' (chosen as 1.0 for numerical evaluation)
a = 1.0

# Compute the Bessel function of the first kind of order 0 at a
bessel_value = mp.besselj(0, a)

# Calculate the constant factor π/(2a)
factor = mp.pi / (2 * a)

# Multiply factor by the Bessel function value
result = factor * bessel_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))