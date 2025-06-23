import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of 'a' (example value, can be adjusted)
a = 1.0

# Compute Bessel functions of the first kind
J0 = mp.besselj(0, a)  # J0(a)
J1 = mp.besselj(1, a)  # J1(a)

# Compute Struve functions
H0 = mp.struveh(0, a)  # H0(a)
H1 = mp.struveh(1, a)  # H1(a)

# Calculate the expression inside the brackets: J0(a)*H1(a) - J1(a)*H0(a)
inner_expr = J0 * H1 - J1 * H0

# Compute the coefficient: (π * a) / 4
coeff = (mp.pi * a) / 4

# Multiply coefficient by the inner expression
product = coeff * inner_expr

# Final result: 1 - product
result = 1 - product

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))