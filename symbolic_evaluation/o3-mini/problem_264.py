import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter 'a' (using a = 1.0 as an example value)
a = 1.0

# Compute the argument for Bessel and Struve functions
arg = a / 2

# Calculate Bessel functions of the first kind
j0 = mp.besselj(0, arg)  # J_0(a/2)
j1 = mp.besselj(1, arg)  # J_1(a/2)

# Calculate Struve functions (Hankel Struve form)
h0 = mp.struveh(0, arg)  # H_0(a/2)
h1 = mp.struveh(1, arg)  # H_1(a/2)

# Compute the expression inside the brackets
bracket_expr = 1 - j0 * h0 + j1 * h1

# Multiply by pi/(2a)
result = (mp.pi / (2 * a)) * bracket_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))