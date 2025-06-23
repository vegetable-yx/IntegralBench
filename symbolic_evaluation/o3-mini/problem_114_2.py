import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Step 1: Compute π^(3/2)
pi_power = mp.power(mp.pi, 1.5)

# Step 2: Compute Gamma(3/4)
gamma_3_4 = mp.gamma(0.75)

# Step 3: Compute Gamma(5/4)
gamma_5_4 = mp.gamma(1.25)

# Step 4: Compute the constant fraction: (π^(3/2) * Gamma(3/4)) / (16 * Gamma(5/4))
fraction = (pi_power * gamma_3_4) / (16 * gamma_5_4)

# Step 5: Compute logarithmic term (6 * ln(2))
log_term = 6 * mp.log(2)

# Step 6: Compute digamma terms: 3 * (digamma(3/4) - digamma(5/4))
digamma_term = 3 * (mp.digamma(0.75) - mp.digamma(1.25))

# Step 7: Combine logarithmic and digamma terms
combined_terms = log_term + digamma_term

# Step 8: Multiply fraction by combined_terms
product = fraction * combined_terms

# Step 9: Apply the negative sign to get final result
result = -product

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))