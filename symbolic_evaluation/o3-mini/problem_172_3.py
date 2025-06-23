import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute gamma(1/4) and raise to the 8th power
gamma_quarter = mp.gamma(mp.mpf(1)/4)
gamma_quarter_8 = gamma_quarter**8

# Compute the logarithmic term: 16 * ln(2) - 3
ln2 = mp.log(2)
log_term = 16 * ln2 - 3

# Numerator: gamma(1/4)^8 * (16*ln(2) - 3)
numerator = gamma_quarter_8 * log_term

# Denominator: 61440 * sqrt(2) * pi^2
sqrt2 = mp.sqrt(2)
pi_squared = mp.pi**2
denominator = 61440 * sqrt2 * pi_squared

# Final result: numerator / denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))