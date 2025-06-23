import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters (user can adjust these values as needed)
a = 1.0
b = 1.0

# Compute gamma function values
gamma_54 = mp.gamma(5/4)  # Γ(5/4)
gamma_34 = mp.gamma(3/4)  # Γ(3/4)
gamma_74 = mp.gamma(7/4)  # Γ(7/4)

# Compute the argument for the hypergeometric function
hyper_arg = (b**4 * a**2) / 256  # b^4 a^2 / 256

# Evaluate the hypergeometric function {}_0F_1(;2; hyper_arg)
hyper_val = mp.hyper([], [2], hyper_arg)  # {}_0F_1(;2; hyper_arg)

# Compute first term: a * Γ(5/4) * Γ(3/4) * {}_0F_1(;2; hyper_arg)
term1 = a * gamma_54 * gamma_34 * hyper_val

# Compute second term: (b^2 * a^2 / 16) * Γ(7/4) * Γ(5/4)
term2 = (b**2 * a**2 / 16) * gamma_74 * gamma_54

# Sum the terms to get final result
result = term1 + term2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))