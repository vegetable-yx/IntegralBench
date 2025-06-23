import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameter 'a' (user can modify this value as needed)
a = mp.mpf(1.0)

# Compute Bessel function of the first kind of order 0 at 'a'
J0 = mp.besselj(0, a)

# Compute Bessel function of the first kind of order 1 at 'a'
J1 = mp.besselj(1, a)

# Calculate the constant term: π/2 multiplied by J1(a)
term_pi_J1 = (mp.pi / 2) * J1

# Compute the numerator: 1 - J0(a) - term_pi_J1
numerator = 1 - J0 - term_pi_J1

# Divide the numerator by a squared to get the final result
result = numerator / (a**2)

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))