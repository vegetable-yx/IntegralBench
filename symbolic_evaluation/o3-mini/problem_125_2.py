import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate gamma(1/4)
gamma_val = mp.gamma(1/4)

# Calculate pi
pi_val = mp.pi

# Compute gamma(1/4) raised to the 4th power
gamma_4 = gamma_val**4

# Compute gamma(1/4) raised to the 8th power (as (gamma^4)^2)
gamma_8 = gamma_4**2

# Compute pi squared
pi_sq = pi_val**2

# Compute pi to the 4th power
pi_4 = pi_sq**2

# Numerator: gamma^8 + 8*pi^2*gamma^4 - 64*pi^4
numerator = gamma_8 + 8 * pi_sq * gamma_4 - 64 * pi_4

# Denominator: 6144 * pi^2
denominator = 6144 * pi_sq

# Final result
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))