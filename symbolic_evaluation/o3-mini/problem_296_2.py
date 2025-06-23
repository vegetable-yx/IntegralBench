import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute gamma functions at required points
gamma_34 = mp.gamma(3/4)   # Γ(3/4)
gamma_14 = mp.gamma(1/4)   # Γ(1/4)

# Compute squares of gamma functions
gamma_34_sq = gamma_34**2  # Γ(3/4)^2
gamma_14_sq = gamma_14**2  # Γ(1/4)^2

# Compute the inner expression: 8√2 * Γ(1/4)^2 - Γ(3/4)^2
inner_expr = 8 * mp.sqrt(2) * gamma_14_sq - gamma_34_sq

# Numerator: Γ(3/4)^2 multiplied by the inner expression
numerator = gamma_34_sq * inner_expr

# Denominator: 96 * √(2π)
denominator = 96 * mp.sqrt(2 * mp.pi)

# Final result
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))