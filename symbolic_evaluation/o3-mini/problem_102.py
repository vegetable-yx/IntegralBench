import mpmath as mp

# Set decimal places for internal computation
mp.dps = 15

# Calculate Gamma(3/4) and Gamma(5/4)
gamma_34 = mp.gamma(3/4)
gamma_54 = mp.gamma(5/4)

# Compute the first term: pi * [Gamma(3/4)]^2 / {8 * [Gamma(5/4)]^2}
numerator = mp.pi * gamma_34**2
denominator = 8 * gamma_54**2
first_term = numerator / denominator

# Compute the argument for the logarithm: sqrt(2) * Gamma(3/4) / Gamma(5/4)
log_argument = (mp.sqrt(2) * gamma_34) / gamma_54

# Compute the second term: (1/2) * ln(log_argument)
second_term = 0.5 * mp.log(log_argument)

# Combine the terms: first_term - second_term
result = first_term - second_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))