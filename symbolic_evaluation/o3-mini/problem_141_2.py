import mpmath as mp

# Set internal decimal precision to 15 for sufficient accuracy
mp.dps = 15

# Define the parameter 'a'. Change this value as needed.
a = 1.0

# Compute the modified Bessel functions of the first kind
# I0(a) = modified Bessel function of order 0
I0 = mp.besseli(0, a)
# I1(a) = modified Bessel function of order 1
I1 = mp.besseli(1, a)

# Compute the modified Struve functions
# L0(a) = modified Struve function of order 0
L0 = mp.struvel(0, a)
# L1(a) = modified Struve function of order 1
L1 = mp.struvel(1, a)

# Compute the expression inside the brackets: I1(a)*L0(a) - I0(a)*L1(a)
bracket_expr = I1 * L0 - I0 * L1

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * bracket_expr

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))