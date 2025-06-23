import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate Gamma(1/4) and raise it to the 8th power
gamma_val = mp.gamma(mp.mpf(1)/4)
gamma_8 = gamma_val**8

# Calculate 16 * pi^2
pi_sq = mp.pi**2
sixteen_pi_sq = 16 * pi_sq

# Numerator: Gamma(1/4)^8 - 16*pi^2
numerator = gamma_8 - sixteen_pi_sq

# Denominator: 9216 * sqrt(pi)
denominator = 9216 * mp.sqrt(mp.pi)

# Final result: numerator divided by denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))