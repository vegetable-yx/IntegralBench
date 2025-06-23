import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute gamma functions at critical points
gamma_14 = mp.gamma(mp.mpf(1)/4)  # Γ(1/4)
gamma_34 = mp.gamma(mp.mpf(3)/4)  # Γ(3/4)

# Precompute squares to avoid redundant calculations
gamma_14_sq = gamma_14**2         # Γ(1/4)^2
gamma_34_sq = gamma_34**2         # Γ(3/4)^2

# Compute sum of squares: Γ(1/4)^2 + Γ(3/4)^2
sum_sq = gamma_14_sq + gamma_34_sq

# Compute common constants involving sqrt(2)
sqrt2 = mp.sqrt(2)
a = 2 + sqrt2          # (2 + √2)
b = 4 + 2*sqrt2        # (4 + 2√2)
c = 3 + 2*sqrt2        # (3 + 2√2)

# Compute each term in the expression
term1 = a * (sum_sq**2)            # (2+√2)(Γ(1/4)^2+Γ(3/4)^2)^2
term2 = b * gamma_14_sq * sum_sq   # (4+2√2)Γ(1/4)^2(Γ(1/4)^2+Γ(3/4)^2)
term3 = c * (gamma_14_sq**2)       # (3+2√2)Γ(1/4)^4

# Combine terms and divide by 256π
numerator = term1 - term2 + term3
result = numerator / (256 * mp.pi)

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))