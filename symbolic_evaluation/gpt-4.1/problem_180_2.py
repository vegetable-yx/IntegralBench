import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate numerator: Bessel function J_{3/2} evaluated at 2
numerator = mp.besselj(1.5, 2)  # Order 3/2 = 1.5

# Calculate denominator: [Gamma(5/4)]^2
gamma_val = mp.gamma(5/4)        # Gamma function at 5/4
denominator = gamma_val ** 2      # Square of Gamma(5/4)

# Compute the final result
result = numerator / denominator

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))