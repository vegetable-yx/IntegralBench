import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Example values for a and b - user should modify these as needed
a = 1.0
b = 1.0

# Compute the common argument: (b^2 * a) / 8
inner_arg = (b**2 * a) / 8.0

# Compute the exponential factor: e^{(b^2 a)/8}
exp_factor = mp.exp(inner_arg)

# Compute the prefactor: sqrt(pi/2)
prefactor = mp.sqrt(mp.pi / 2.0)

# Compute the first term: (8/(b^2 a))^{1/4} * Gamma(3/4) * I_{-1/4}(inner_arg)
# Note: (8/(b^2 a))^{1/4} = (1/inner_arg)^{1/4} = inner_arg^{-0.25}
term1_coeff = inner_arg ** (-0.25)
gamma1 = mp.gamma(0.75)  # Gamma(3/4)
bessel1 = mp.besseli(-0.25, inner_arg)  # I_{-1/4}(inner_arg)
term1 = term1_coeff * gamma1 * bessel1

# Compute the second term: (b^2 a / 8)^{1/4} * Gamma(1/4) * I_{1/4}(inner_arg)
# Note: (b^2 a / 8)^{1/4} = inner_arg^{0.25}
term2_coeff = inner_arg ** 0.25
gamma2 = mp.gamma(0.25)  # Gamma(1/4)
bessel2 = mp.besseli(0.25, inner_arg)  # I_{1/4}(inner_arg)
term2 = term2_coeff * gamma2 * bessel2

# Combine terms inside the brackets
bracket = term1 + term2

# Multiply all components: prefactor * exp_factor * bracket
result = prefactor * exp_factor * bracket

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))