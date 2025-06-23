import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant pi/4
pi_over_4 = mp.pi / 4

# Compute Bessel function J0 at 1
j0_at_1 = mp.besselj(0, 1)

# Square the Bessel function value
j0_squared = j0_at_1 ** 2

# Compute the expression: (pi/4) * (1 - [J0(1)]^2)
result = pi_over_4 * (1 - j0_squared)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))