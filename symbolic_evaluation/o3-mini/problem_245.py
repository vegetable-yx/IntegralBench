import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Compute Γ(1/4)
gamma_1_4 = mp.gamma(1/4)

# Compute π
pi = mp.pi

# Compute intermediate powers of gamma_1_4
gamma_1_4_4 = gamma_1_4**4  # Γ(1/4)^4
gamma_1_4_8 = gamma_1_4_4**2  # Γ(1/4)^8

# Compute powers of π
pi_2 = pi**2  # π^2
pi_4 = pi_2**2  # π^4

# Compute the three terms in the numerator
term1 = gamma_1_4_8
term2 = 32 * pi_2 * gamma_1_4_4
term3 = 768 * pi_4

# Sum the terms to get the numerator
numerator = term1 + term2 + term3

# Compute the denominator: 23040 * π^4
denominator = 23040 * pi_4

# Compute the final result
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))