import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Define the value of the parameter 'a'
a = mp.mpf(1.0)

# Compute Bessel functions of the first kind
J0 = mp.besselj(0, a)  # J0(a)
J1 = mp.besselj(1, a)  # J1(a)

# Compute Struve functions (H0 and H1)
H0 = mp.struveh(0, a)  # H0(a)
H1 = mp.struveh(1, a)  # H1(a)

# Compute the expression inside the brackets: J1(a)*H0(a) - J0(a)*H1(a)
bracket_term = J1 * H0 - J0 * H1

# Compute the entire expression: (π/(2a)) * bracket_term
result = (mp.pi / (2 * a)) * bracket_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))