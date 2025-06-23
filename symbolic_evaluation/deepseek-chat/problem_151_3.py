import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate numerator: pi raised to the power of 3/2
numerator = mp.power(mp.pi, 1.5)

# Calculate Gamma(3/4)
gamma_val = mp.gamma(0.75)

# Square the Gamma function value
gamma_sq = mp.power(gamma_val, 2)

# Calculate denominator: sqrt(2) multiplied by Gamma(3/4)^2
denominator = mp.sqrt(2) * gamma_sq

# Compute the result: numerator divided by denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))