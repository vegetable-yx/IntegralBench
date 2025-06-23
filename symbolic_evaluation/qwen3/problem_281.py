import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate numerator components
two_power = 2**(5/2)          # 2^(5/2)
pi_power = mp.pi**(3/2)       # π^(3/2)
numerator = two_power * pi_power  # Combine numerator terms

# Calculate denominator components
gamma_term = mp.gamma(1/4)    # Γ(1/4)
denominator = gamma_term**2    # Square of gamma term

# Compute final result
result = numerator / denominator

print(mp.nstr(result, n=10))