import mpmath as mp
mp.dps = 15

# Calculate Gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Square the Gamma function result
gamma_squared = gamma_val ** 2

# Compute denominator: sqrt(8*pi)
denominator = mp.sqrt(8 * mp.pi)

# Calculate the fractional component
fraction_part = gamma_squared / denominator

# Compute exponential component e^4
exp_component = mp.exp(4)

# Combine all components for final result
result = fraction_part * exp_component

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))