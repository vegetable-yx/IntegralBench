import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant factor: sqrt(2*pi)/2
factor = mp.sqrt(2 * mp.pi) / 2

# Compute Gamma function values
gamma_3_4 = mp.gamma(3/4)
gamma_5_4 = mp.gamma(5/4)
gamma_7_4 = mp.gamma(7/4)

# Compute coefficients for the Bessel function terms
coeff1 = gamma_3_4 / gamma_5_4
coeff2 = gamma_5_4 / gamma_7_4

# Evaluate Bessel functions at z=1
bessel_minus_1_4 = mp.besselj(-1/4, 1)
bessel_1_4 = mp.besselj(1/4, 1)

# Compute the two terms inside the parentheses
term1 = coeff1 * bessel_minus_1_4
term2 = coeff2 * bessel_1_4

# Combine the terms and multiply by the constant factor
result = factor * (term1 - term2)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))