import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter 'a' (example value, can be changed as needed)
a = 1.0

# Compute Bessel function J0(a)
j0_val = mp.besselj(0, a)

# Compute the expression (1 + J0(a))
one_plus_j0 = 1 + j0_val

# Compute the constant factor pi/(2a)
pi_over_2a = mp.pi / (2 * a)

# Multiply to get the final result
result = pi_over_2a * one_plus_j0

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))