import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of 'a' (example value, can be changed)
a = 1.0

# Calculate the first term: sin(a) / a^2
sin_a = mp.sin(a)
a_squared = a**2
term1 = sin_a / a_squared

# Calculate the second term: (π / (2a^2)) * J_1(a)
pi = mp.pi
bessel_term = mp.besselj(1, a)  # Bessel function of first kind order 1
term2 = (pi / (2 * a_squared)) * bessel_term

# Combine terms: result = term1 - term2
result = term1 - term2

# Print final result to 10 decimal places
print(mp.nstr(result, n=10))