import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute the constant factor: 2^(-1/2) = 1/sqrt(2)
factor = mp.power(2, -0.5)

# Compute Gamma(1/4)
gamma_14 = mp.gamma(mp.mpf(1)/4)

# Compute Gamma(3/4)
gamma_34 = mp.gamma(mp.mpf(3)/4)

# Compute modified Bessel function I_{-1/4}(1/2)
bessel_neg14 = mp.besseli(-mp.mpf(1)/4, 0.5)

# Compute modified Bessel function I_{1/4}(1/2)
bessel_14 = mp.besseli(mp.mpf(1)/4, 0.5)

# Calculate the expression inside the brackets: 
# Gamma(1/4)*I_{-1/4}(1/2) - Gamma(3/4)*I_{1/4}(1/2)
inner_expr = gamma_14 * bessel_neg14 - gamma_34 * bessel_14

# Multiply by the constant factor
result = factor * inner_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))