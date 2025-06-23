import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of 'a' (change this value as needed for different evaluations)
a_val = 1.0
a = mp.mpf(a_val)

# Compute Bessel functions of the first kind
J0 = mp.besselj(0, a)  # J_0(a)
J1 = mp.besselj(1, a)  # J_1(a)

# Compute Struve functions (Hankel type)
H0 = mp.struveh(0, a)  # H_0(a)
H1 = mp.struveh(1, a)  # H_1(a)

# Compute the term: J0(a)*H1(a) + J1(a)*H0(a)
term = J0 * H1 + J1 * H0

# Compute the expression: 1/a^2 - (pi/(2a)) * [J0(a)*H1(a) + J1(a)*H0(a)]
result = 1/(a**2) - (mp.pi/(2*a)) * term

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))