import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate 2^(5/4) using mpmath power function
two_power = mp.power(2, mp.mpf(5)/4)

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate Gamma(1/4) and square it
gamma_value = mp.gamma(mp.mpf(1)/4)
gamma_squared = gamma_value ** 2

# Combine all components for final result
result = two_power * sqrt_pi * gamma_squared

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))