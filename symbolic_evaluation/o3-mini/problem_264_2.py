import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Define the value of a (example value, can be changed by user)
a = 1.0

# Compute Bessel function of the first kind, order 0
j0 = mp.besselj(0, a)

# Compute Bessel function of the first kind, order 1
j1 = mp.besselj(1, a)

# Compute Struve function, order 0
h0 = mp.struveh(0, a)

# Compute Struve function, order 1
h1 = mp.struveh(1, a)

# Calculate the term inside the brackets: J0(a)*H0(a) - J1(a)*H1(a)
bracket_term = j0 * h0 - j1 * h1

# Multiply bracket term by pi
pi_bracket = mp.pi * bracket_term

# Compute numerator: π*(J0*H0 - J1*H1) - 2*J1
numerator = pi_bracket - 2 * j1

# Compute denominator: 2a
denominator = 2 * a

# Final result calculation
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))