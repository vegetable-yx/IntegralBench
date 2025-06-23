import mpmath as mp

mp.dps = 15  # Set internal decimal precision

# Calculate components of the expression
sqrt_pi = mp.sqrt(mp.pi)  # Square root of pi
bessel_0 = mp.besseli(0, 5)  # Modified Bessel function I_0(5)
bessel_1 = mp.besseli(1, 5)  # Modified Bessel function I_1(5)

# Compute the polynomial combination of Bessel functions
bessel_combination = 5 * bessel_0 - bessel_1

# Calculate the final result
result = (5 * sqrt_pi / 2) * bessel_combination

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))