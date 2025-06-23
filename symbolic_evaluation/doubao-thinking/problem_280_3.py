import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate Gamma(1/4) and square it
gamma_1_4 = mp.gamma(mp.mpf(1)/4)
gamma_squared = gamma_1_4 ** 2

# Calculate denominator components
two_power = 2 ** (mp.mpf(3)/2)  # 2^(3/2)
three_power = 3 ** (mp.mpf(1)/4)  # 3^(1/4)
denominator = two_power * three_power

# Combine numerator and denominator
numerator = mp.pi * gamma_squared
result = numerator / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))