import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi raised to the power of 3/2
pi_term = mp.pi**(mp.mpf(3)/2)

# Calculate Gamma(3/4)
gamma_val = mp.gamma(mp.mpf(3)/4)

# Square the Gamma function value
gamma_sq = gamma_val**2

# Calculate denominator: sqrt(2) * [Gamma(3/4)]^2
denom = mp.sqrt(2) * gamma_sq

# Compute the final result: pi^(3/2) / [sqrt(2) * Gamma(3/4)^2]
result = pi_term / denom

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))