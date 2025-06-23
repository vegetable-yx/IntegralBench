import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of 'a' (user can modify this value as needed)
a = 1.0

# Calculate intermediate terms step by step
# Compute 2 - π
two_minus_pi = 2 - mp.pi

# Compute J₀(a) - Bessel function of the first kind (order 0)
bessel_j0 = mp.besselj(0, a)

# Compute 1 - J₀(a)
one_minus_bessel = 1 - bessel_j0

# Numerator: (2 - π) * (1 - J₀(a))
numerator = two_minus_pi * one_minus_bessel

# Denominator: 2a²
denominator = 2 * (a ** 2)

# Final result: numerator divided by denominator
result = numerator / denominator

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))