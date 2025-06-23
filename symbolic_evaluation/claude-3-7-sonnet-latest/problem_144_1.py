import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute the value of the modified Bessel function of the first kind of order 0 at 2
bessel_val = mp.besseli(0, 2)

# Compute the expression inside the parentheses: (1 - I_0(2))
inner_expr = 1 - bessel_val

# Multiply by pi/8: result = (pi/8) * (1 - I_0(2))
result = (mp.pi / 8) * inner_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))