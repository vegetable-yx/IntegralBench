import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute Bessel function of the first kind, order 0 at z=1
j0 = mp.besselj(0, 1)

# Compute Bessel function of the first kind, order 1 at z=1
j1 = mp.besselj(1, 1)

# Compute Struve function, order 0 at z=1
h0 = mp.struveh(0, 1)

# Compute Struve function, order 1 at z=1
h1 = mp.struveh(1, 1)

# Calculate the expression inside the brackets: J0(1)*H1(1) - J1(1)*H0(1)
inner_expr = j0 * h1 - j1 * h0

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * inner_expr

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))