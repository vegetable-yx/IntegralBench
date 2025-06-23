import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Define the parameter 'a' (example value, can be changed as needed)
a = 1.0

# Compute pi constant
pi_val = mp.pi

# Compute J_0(a) - Bessel function of the first kind of order 0
bessel_j0 = mp.besselj(0, a)

# Compute the numerator: (π - 2) * (1 - J_0(a))
numerator = (pi_val - 2) * (1 - bessel_j0)

# Compute the denominator: 2 * a^2
denominator = 2 * a**2

# Compute the final result: numerator / denominator
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))