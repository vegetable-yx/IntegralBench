import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate J0(1) - Bessel function of the first kind of order 0 at 1
bessel_j0_1 = mp.besselj(0, 1)

# Square the Bessel function value
bessel_sq = bessel_j0_1 ** 2

# Compute the expression inside the parentheses: 1 - J0(1)^2
inner_expr = 1 - bessel_sq

# Multiply by π/4 to get the final result
result = (mp.pi / 4) * inner_expr

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))