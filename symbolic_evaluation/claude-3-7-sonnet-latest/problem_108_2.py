import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate the numerator: 4 * (2^(3/2))
numerator = 4 * mp.power(2, mp.mpf('1.5'))

# Calculate the denominator: 3 * π^2
denominator = 3 * mp.power(mp.pi, 2)

# Compute Γ(1/4) and square it
gamma_term = mp.gamma(mp.mpf('0.25'))
gamma_squared = mp.power(gamma_term, 2)

# Combine components: (numerator / denominator) * gamma_squared
result = (numerator / denominator) * gamma_squared

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))