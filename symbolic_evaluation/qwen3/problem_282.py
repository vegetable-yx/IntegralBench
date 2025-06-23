import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 2^(3/2)
two_power = mp.power(2, 1.5)

# Calculate sqrt(pi)
sqrt_pi = mp.sqrt(mp.pi)

# Combine numerator components
numerator = two_power * sqrt_pi

# Calculate Gamma(3/4) and square it
gamma_3_4 = mp.gamma(mp.mpf(3)/4)
denominator = gamma_3_4 ** 2

# Compute the fraction (2^(3/2) * sqrt(pi)) / (Gamma(3/4)^2)
fraction = numerator / denominator

# Calculate hyperbolic cosine of 4
cosh_4 = mp.cosh(4)

# Final result calculation
result = fraction * cosh_4

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))