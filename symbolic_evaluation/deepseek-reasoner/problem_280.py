import mpmath as mp

mp.dps = 15  # Set internal precision

# Example values for a and b (modify as needed)
a = mp.mpf('1')
b = mp.mpf('1')

sqrt_a = mp.sqrt(a)
gamma_term = 2 * mp.gamma(mp.mpf(3)/4) ** 2
pi_sqrt = mp.sqrt(mp.pi)
hyper_z = (a * b) ** 2 / 16

# Calculate hypergeometric function 1F2 parameters: [3/4], [5/4, 1/2], z
hyper_part = mp.hyper([mp.mpf(3)/4], [mp.mpf(5)/4, mp.mpf(1)/2], hyper_z)

# Combine all components
result = sqrt_a * gamma_term / pi_sqrt * hyper_part

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))