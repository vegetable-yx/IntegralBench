import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the expression
sqrt_pi = mp.sqrt(mp.pi)  # Compute square root of pi
gamma_3_4 = mp.gamma(mp.mpf(3)/4)  # Gamma function at 3/4
gamma_1_4 = mp.gamma(mp.mpf(1)/4)  # Gamma function at 1/4
two_power = mp.power(2, mp.mpf(3)/4)  # 2 raised to 3/4 power

# Combine components using intermediate calculations
denominator = gamma_3_4 ** 2  # Square of Gamma(3/4)
numerator = sqrt_pi * two_power * gamma_1_4  # Combined numerator
result = numerator / denominator  # Final division

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))