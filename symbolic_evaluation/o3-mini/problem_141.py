import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of 'a' (user can modify this as needed)
a = 1.0

# Compute modified Bessel function of first kind order 0
I0 = mp.besseli(0, a)

# Compute modified Bessel function of first kind order 1
I1 = mp.besseli(1, a)

# Compute modified Struve function order 0
L0 = mp.struvel(0, a)

# Compute modified Struve function order 1
L1 = mp.struvel(1, a)

# Calculate the expression inside the brackets
bracket_expr = I0 * L1 - I1 * L0

# Multiply by pi/2 to get final result
result = (mp.pi / 2) * bracket_expr

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))