import mpmath as mp
mp.dps = 15  # Set decimal precision for intermediate calculations

# Compute Gamma(1/4)
gamma_value = mp.gamma(mp.mpf('1/4'))

# Raise Gamma(1/4) to the 4th power
gamma_power = gamma_value**4

# Calculate the constant denominator components
sqrt_two = mp.sqrt(2)
denominator = 4 * sqrt_two * mp.pi

# Compute the final result by dividing numerator and denominator
result = gamma_power / denominator

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))