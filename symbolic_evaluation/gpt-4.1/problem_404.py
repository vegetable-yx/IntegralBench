import mpmath as mp

# Set the internal decimal precision to 15 for calculations
mp.dps = 15

# Compute the first term: (1/25) * [Γ(1/25) * Γ(21/20) / Γ(1/25 + 21/20)]
# Step 1: Calculate the sum of arguments for the denominator: 1/25 + 21/20
a1 = mp.mpf(1)/25
b1 = mp.mpf(21)/20
denom1 = a1 + b1

# Step 2: Compute gamma functions for numerator and denominator
gamma_a1 = mp.gamma(a1)
gamma_b1 = mp.gamma(b1)
gamma_denom1 = mp.gamma(denom1)

# Step 3: Combine to form the fraction part
frac1 = gamma_a1 * gamma_b1 / gamma_denom1

# Step 4: Multiply by 1/25
term1 = (mp.mpf(1)/25) * frac1

# Compute the second term: (1/20) * [Γ(1/20) * Γ(26/25) / Γ(1/20 + 26/25)]
# Step 1: Calculate the sum of arguments for the denominator: 1/20 + 26/25
a2 = mp.mpf(1)/20
b2 = mp.mpf(26)/25
denom2 = a2 + b2

# Step 2: Compute gamma functions for numerator and denominator
gamma_a2 = mp.gamma(a2)
gamma_b2 = mp.gamma(b2)
gamma_denom2 = mp.gamma(denom2)

# Step 3: Combine to form the fraction part
frac2 = gamma_a2 * gamma_b2 / gamma_denom2

# Step 4: Multiply by 1/20
term2 = (mp.mpf(1)/20) * frac2

# Final result: term1 - term2
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))