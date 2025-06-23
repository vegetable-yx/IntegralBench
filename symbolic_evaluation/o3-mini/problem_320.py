import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Example value for 'a' (can be changed by the user)
a = 2.0

# Compute the first term: 2 / a
term1 = mp.mpf(2) / a

# Compute Struve functions: H0(a) and H1(a)
H0 = mp.struveh(0, a)
H1 = mp.struveh(1, a)

# Compute Bessel functions of the second kind: Y0(a) and Y1(a)
Y0 = mp.bessely(0, a)
Y1 = mp.bessely(1, a)

# Compute the expression inside the brackets: [H0(a)*Y1(a) - H1(a)*Y0(a)]
bracket_expr = H0 * Y1 - H1 * Y0

# Compute the second term: (π/2) * bracket_expr
term2 = (mp.pi / 2) * bracket_expr

# Final result: term1 - term2
result = term1 - term2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))