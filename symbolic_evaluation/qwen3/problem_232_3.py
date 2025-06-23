import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate numerator components
two_power = mp.power(2, 7/4)  # 2^(7/4)
sqrt_pi = mp.sqrt(mp.pi)      # Square root of pi
numerator = two_power * sqrt_pi

# Calculate denominator components
gamma_34 = mp.gamma(3/4)      # Gamma function at 3/4
denominator = gamma_34 ** 2   # Square of Gamma(3/4)

# Compute final result
result = numerator / denominator

# Print result to 10 decimal places
print(mp.nstr(result, n=10))