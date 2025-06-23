import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Bessel function of the first kind of order 0 at x=1
j0_val = mp.besselj(0, 1)

# Compute Bessel function of the first kind of order 2 at x=1
j2_val = mp.besselj(2, 1)

# Compute the expression inside the parentheses: 7*J0(1) + 6*J2(1)
inner_expr = 7 * j0_val + 6 * j2_val

# Multiply by pi/8
term1 = (mp.pi / 8) * inner_expr

# Compute Bessel function of the first kind of order 1 at x=1
j1_val = mp.besselj(1, 1)

# Final result: term1 minus J1(1)
result = term1 - j1_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))