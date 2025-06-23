import mpmath as mp

# Set internal decimal places to 15 for precision
mp.dps = 15

# Calculate gamma(1/4)
gamma_val = mp.gamma(0.25)

# Compute gamma(1/4)^4
gamma_fourth = gamma_val**4

# Compute pi squared
pi_sq = mp.pi**2

# Compute 2 * pi squared
two_pi_sq = 2 * pi_sq

# Numerator: gamma(1/4)^4 - 2*pi^2
numerator = gamma_fourth - two_pi_sq

# Calculate denominator components
# 24 * sqrt(2)
const_part = 24 * mp.sqrt(2)

# pi^(3/2) = pi * sqrt(pi)
pi_power = mp.pi * mp.sqrt(mp.pi)

# Full denominator: 24 * sqrt(2) * pi^(3/2)
denominator = const_part * pi_power

# Final result: numerator divided by denominator
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))