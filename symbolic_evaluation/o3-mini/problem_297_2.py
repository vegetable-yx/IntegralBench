import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute gamma function values
gamma_1_4 = mp.gamma(mp.mpf(1)/4)
gamma_7_4 = mp.gamma(mp.mpf(7)/4)

# Compute numerator: π^(3/2) * [Γ(1/4)]^2
pi_sqrt = mp.sqrt(mp.pi)  # π^(1/2)
pi_power = pi_sqrt * mp.pi  # π^(3/2)
numerator = pi_power * gamma_1_4**2

# Compute denominator: 64 * [Γ(7/4)]^2
denominator = 64 * gamma_7_4**2

# Compute the coefficient: numerator / denominator
coeff = numerator / denominator

# Compute hypergeometric function values
hyp1 = mp.hyp2f1(mp.mpf(-1)/2, mp.mpf(1)/2, mp.mpf(3)/4, mp.mpf(1)/2)
hyp2 = mp.hyp2f1(mp.mpf(-1)/2, mp.mpf(1)/2, mp.mpf(7)/4, mp.mpf(1)/2)

# Compute the difference: hyp1 - hyp2
diff = hyp1 - hyp2

# Multiply coefficient by the difference to get final result
result = coeff * diff

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))