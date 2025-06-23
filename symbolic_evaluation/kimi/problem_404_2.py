import mpmath as mp

mp.dps = 15  # Set internal precision for calculations

# Calculate first term components
term1_coeff = mp.mpf(1)/25
gamma_num1 = mp.gamma(mp.mpf(1)/25) * mp.gamma(mp.mpf(21)/20)
gamma_den1 = mp.gamma(mp.mpf(1)/25 + mp.mpf(21)/20)
term1 = term1_coeff * (gamma_num1 / gamma_den1)

# Calculate second term components
term2_coeff = mp.mpf(1)/20
gamma_num2 = mp.gamma(mp.mpf(1)/20) * mp.gamma(mp.mpf(26)/25)
gamma_den2 = mp.gamma(mp.mpf(1)/20 + mp.mpf(26)/25)
term2 = term2_coeff * (gamma_num2 / gamma_den2)

# Compute final result
result = term1 - term2

# Print with exactly 10 decimal places
print(mp.nstr(result, n=10))