import mpmath as mp

mp.dps = 15  # Set internal precision for calculations

# Compute Bessel function J0 at 1
j0_1 = mp.besselj(0, 1)

# Square the Bessel function value
j0_squared = j0_1 ** 2

# Calculate the (1 - J0(1)^2) term
one_minus_j0_sq = 1 - j0_squared

# Multiply by π/4 to get the final result
result = (mp.pi / 4) * one_minus_j0_sq

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))