import mpmath as mp

# Set internal decimal precision to 15 to ensure accurate computation
mp.dps = 15

# Define the parameters for the hypergeometric function
a1 = mp.mpf(-0.5)  # First parameter: -1/2
a2 = mp.mpf(0.5)   # Second parameter: 1/2
a3 = mp.mpf(0.5)   # Third parameter: 1/2
b1 = mp.mpf(1)     # Fourth parameter: 1
b2 = mp.mpf(1.5)   # Fifth parameter: 3/2
z = mp.mpf(0.25)   # Argument: 1/4

# Compute the generalized hypergeometric function _3F_2
hyper_val = mp.hyper3f2(a1, a2, a3, b1, b2, z)

# Compute the constant factor: π² / 8
pi_sq_over_8 = mp.pi**2 / 8

# Multiply the constant factor by the hypergeometric function
result = pi_sq_over_8 * hyper_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))