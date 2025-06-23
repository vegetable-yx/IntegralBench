import mpmath as mp

# Set precision to 15 decimal places
mp.dps = 15

# Define the parameter 'a'. Change this value as needed for different evaluations.
a = mp.mpf(1.0)

# Compute Bessel functions of the first kind
J0 = mp.besselj(0, a)  # J_0(a)
J1 = mp.besselj(1, a)  # J_1(a)

# Compute Struve functions (Hankel type)
H0 = mp.struveh(0, a)  # H_0(a)
H1 = mp.struveh(1, a)  # H_1(a)

# Calculate the expression inside the brackets
inner_expr = J0 * H0 - J1 * H1

# Compute the prefactor: π/(2a)
prefactor = mp.pi / (2 * a)

# Combine to get the final result
result = prefactor * inner_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))