import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Define the argument for the functions
z = mp.mpf('0.5')

# Calculate the fractional orders as mpmath floats
v1 = mp.mpf('0.25')   # 1/4
v2 = mp.mpf('-0.25')  # -1/4

# Compute Bessel functions of the first kind
J_14 = mp.besselj(v1, z)   # J_{1/4}(1/2)
J_m14 = mp.besselj(v2, z)  # J_{-1/4}(1/2)

# Compute Struve functions (Hankel Struve as per requirement)
H_m14 = mp.struveh(v2, z)  # H_{-1/4}(1/2)
H_14 = mp.struveh(v1, z)   # H_{1/4}(1/2)

# Compute the combination inside the brackets
inner_expr = J_14 * H_m14 - J_m14 * H_14

# Calculate the constant factor: -π√2 / 4
factor = -mp.pi * mp.sqrt(2) / 4

# Multiply the inner expression by the factor to get the result
result = factor * inner_expr

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))