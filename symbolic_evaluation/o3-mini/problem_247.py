import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute gamma(1/4)
gamma_14 = mp.gamma(1/4)

# Compute pi constant
pi_val = mp.pi

# Calculate term1: Γ(1/4)^8 / (1024 * π^2)
gamma_14_power8 = gamma_14**8
pi_squared = pi_val**2
term1 = gamma_14_power8 / (1024 * pi_squared)

# Calculate term2: Γ(1/4)^4 / (64 * sqrt(2π))
gamma_14_power4 = gamma_14**4
sqrt_2pi = mp.sqrt(2 * pi_val)
denominator_term2 = 64 * sqrt_2pi
term2 = gamma_14_power4 / denominator_term2

# Calculate term3: π / 128
term3 = pi_val / 128

# Sum all terms to get final result
result = term1 + term2 + term3

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))