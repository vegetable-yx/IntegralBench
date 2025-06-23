import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of 'a' (can be adjusted as needed)
a_val = 1.0

# Compute Bessel functions of the first kind
J0 = mp.besselj(0, a_val)  # J_0(a)
J1 = mp.besselj(1, a_val)  # J_1(a)
J2 = mp.besselj(2, a_val)  # J_2(a)

# Compute modified Struve functions
L0 = mp.struvel(0, a_val)  # L_0(a)
L1 = mp.struvel(1, a_val)  # L_1(a)

# Calculate intermediate terms
term1 = 2 * J0 * L1           # 2J_0(a)L_1(a)
term2 = J1 * L0                # J_1(a)L_0(a)
term3 = (a_val / 2) * (J0 + J2) * L0  # (a/2)(J_0(a) + J_2(a))L_0(a)

# Combine terms for the bracket expression
bracket_expr = term1 - term2 - term3

# Compute the prefactor: π/(2a²)
prefactor = mp.pi / (2 * a_val**2)

# Multiply by the prefactor to get the final result
result = prefactor * bracket_expr

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))