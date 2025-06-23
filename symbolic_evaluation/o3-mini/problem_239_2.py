import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter 'a'. Change this value as needed.
a = mp.mpf(1.0)

# Compute modified Bessel functions of the first kind
I0 = mp.besseli(0, a)  # I_0(a)
I1 = mp.besseli(1, a)  # I_1(a)

# Compute modified Struve functions
L0 = mp.struvel(0, a)  # L_0(a)
L1 = mp.struvel(1, a)  # L_1(a)

# Calculate the expression inside the square brackets: I0*L1 - I1*L0
bracket_term = I0 * L1 - I1 * L0

# Multiply by pi: pi * (I0*L1 - I1*L0)
pi_times_bracket = mp.pi * bracket_term

# Subtract 2: pi*(I0*L1 - I1*L0) - 2
inner_expr = pi_times_bracket - 2

# Divide by 2a: [inner_expr] / (2a)
result = inner_expr / (2 * a)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))