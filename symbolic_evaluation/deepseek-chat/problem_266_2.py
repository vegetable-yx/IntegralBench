import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate the Bessel function of the first kind of order 0 at 2
j0_val = mp.besselj(0, 2)

# Compute the expression inside the parentheses: 1 - J0(2)
inner_expr = 1 - j0_val

# Multiply by pi/4 to get the final result
result = (mp.pi / 4) * inner_expr

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))