import mpmath as mp

mp.dps = 15  # Set internal precision

# Example parameters (adjust values as needed)
a = 1.0
b = 1.0

# Calculate common components
sqrt_a_over_2 = mp.sqrt(a / 2)
bessel_argument = b * sqrt_a_over_2

# Compute first term components
term1_coeff = (a * mp.pi) / mp.sqrt(2)
term1_bessel = mp.besseli(0, bessel_argument)

# Compute second term components
term2_coeff = (mp.pi * mp.sqrt(a)) / b
term2_bessel = mp.besseli(1, bessel_argument)

# Combine terms for final result
result = term1_coeff * term1_bessel - term2_coeff * term2_bessel

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))