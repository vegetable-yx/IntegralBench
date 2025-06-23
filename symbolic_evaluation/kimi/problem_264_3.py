import mpmath as mp

mp.dps = 15  # Set internal decimal precision to 15

# Compute Bessel functions of the first kind at order 0 and 2 for argument 2
J0_2 = mp.besselj(0, 2)
J2_2 = mp.besselj(2, 2)

# Calculate the combination of Bessel functions and constants
bessel_combination = J0_2 - J2_2 - 1

# Multiply by π/4 to get the final result
result = (mp.pi / 4) * bessel_combination

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))