import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute gamma(1/4)
gamma_val = mp.gamma(mp.mpf(1)/4)

# Compute gamma(1/4)^8
gamma8 = gamma_val**8

# Compute pi^8
pi8 = mp.pi**8

# Compute the numerator: gamma(1/4)^8 + (1024 * pi^8) / gamma(1/4)^8
numerator = gamma8 + (1024 * pi8) / gamma8

# Compute denominator: 6144 * pi^2
denominator = 6144 * (mp.pi**2)

# Final result
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))