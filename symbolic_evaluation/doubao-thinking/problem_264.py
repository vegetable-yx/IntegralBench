import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate Bessel function of the first kind of order 0 at 1
j0_1 = mp.besselj(0, 1)

# Square the Bessel function value
j0_1_squared = j0_1 ** 2

# Calculate the (1 - J0(1)^2) term
one_minus_squared = 1 - j0_1_squared

# Multiply by π/4 to get final result
result = (mp.pi / 4) * one_minus_squared

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))