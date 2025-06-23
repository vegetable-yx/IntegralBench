import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate 2^(3/2) = 2*sqrt(2)
base_factor = mp.power(2, 1.5)

# Compute Gamma(5/4) = Gamma(1.25)
gamma_5_4 = mp.gamma(1.25)

# Square Gamma(5/4)
gamma_sq = gamma_5_4 ** 2

# Compute Gamma(7/4) = Gamma(1.75)
gamma_7_4 = mp.gamma(1.75)

# Compute the ratio [Gamma(5/4)]^2 / Gamma(7/4)
gamma_ratio = gamma_sq / gamma_7_4

# Compute Bessel function J_{3/2}(2)
bessel_j = mp.besselj(1.5, 2)  # Order 3/2 = 1.5

# Multiply all components: 2^(3/2) * (ratio) * J_{3/2}(2)
result = base_factor * gamma_ratio * bessel_j

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))