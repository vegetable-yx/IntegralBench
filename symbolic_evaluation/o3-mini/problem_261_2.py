import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of 'a' (using example value a=1.0)
a = 1.0

# Compute Bessel function of the first kind J0(a)
J0 = mp.besselj(0, a)

# Compute modified Struve function L1(a)
L1 = mp.struvel(1, a)

# Compute Bessel function of the first kind J1(a)
J1 = mp.besselj(1, a)

# Compute modified Struve function L0(a)
L0 = mp.struvel(0, a)

# Calculate J0(a)*L1(a)
term1 = J0 * L1

# Calculate J1(a)*L0(a)
term2 = J1 * L0

# Compute the expression inside the brackets: J0(a)L1(a) - J1(a)L0(a)
inner_expr = term1 - term2

# Multiply by π/2
factor = (mp.pi / 2) * inner_expr

# Add 1 to complete the expression
result = 1 + factor

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))