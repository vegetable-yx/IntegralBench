import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute gamma functions
gamma_3_4 = mp.gamma(mp.mpf('3/4'))  # Gamma(3/4)
gamma_5_4 = mp.gamma(mp.mpf('5/4'))  # Gamma(5/4)

# Compute pi^(3/2)
pi_sq = mp.sqrt(mp.pi)  # pi^(1/2)
pi_power = mp.pi * pi_sq  # pi^(3/2) = pi * pi^(1/2)

# Compute the constant factor: pi^(3/2) * Gamma(3/4) / (2√2 * Gamma(5/4))
denominator = 2 * mp.sqrt(2) * gamma_5_4
constant_factor = pi_power * gamma_3_4 / denominator

# Compute the hypergeometric function ₂F₁(-1/2, 1/4; 5/4; 1/4)
hyp_val = mp.hyp2f1(mp.mpf('-1/2'), mp.mpf('1/4'), mp.mpf('5/4'), mp.mpf('1/4'))

# Multiply constant factor by hypergeometric value
result = constant_factor * hyp_val

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))