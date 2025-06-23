import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Define the value of a (example value, can be changed by the user)
a = 1.0

# Compute Bessel functions of the first kind
J0 = mp.besselj(0, a)  # J0(a)
J1 = mp.besselj(1, a)  # J1(a)

# Compute Struve functions (Hankel Struve H_v)
H0 = mp.struveh(0, a)  # Struve H_0(a)
H1 = mp.struveh(1, a)  # Struve H_1(a)

# Compute the inner product: J0(a)*H1(a) + J1(a)*H0(a)
inner_product = J0 * H1 + J1 * H0

# Multiply by pi/2
pi_factor = (mp.pi / 2) * inner_product

# Compute the expression inside the brackets: (pi_factor - 1)
bracket_expr = pi_factor - 1

# Multiply by a/4 to get the final result
result = (a / 4) * bracket_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))