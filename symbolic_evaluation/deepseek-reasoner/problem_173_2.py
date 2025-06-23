import mpmath as mp
mp.dps = 15

# Calculate dilogarithm term Li₂(1/4)
li2_term = mp.polylog(2, mp.mpf(1)/4)

# Calculate logarithmic term 3*ln(4/3)
log_term = 3 * mp.log(mp.mpf(4)/3)

# Combine all components
combined_terms = li2_term + log_term - 1

# Multiply by π/8 for final result
result = (mp.pi / 8) * combined_terms

print(mp.nstr(result, n=10))