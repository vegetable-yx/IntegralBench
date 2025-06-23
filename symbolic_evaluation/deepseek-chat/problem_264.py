import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of parameter 'a' (example value, can be changed)
a = 1.0

# Calculate the argument for the Bessel function (a/2)
half_a = a / 2.0

# Compute the Bessel function of the first kind of order 0 at half_a
j0_half = mp.besselj(0, half_a)

# Square the Bessel function value
j0_squared = j0_half ** 2

# Compute the constant factor: pi/(2a)
pi_over_2a = mp.pi / (2.0 * a)

# Compute the entire expression: (pi/(2a)) * (1 - [J0(a/2)]^2)
result = pi_over_2a * (1.0 - j0_squared)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))