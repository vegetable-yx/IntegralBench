import mpmath as mp
mp.dps = 15

# Calculate 3*ln(4/3) component
log_term = mp.log(mp.mpf(4)/3)
three_log = 3 * log_term

# Calculate dilogarithm term Li₂(1/4)
li2_term = mp.polylog(2, mp.mpf(1)/4)

# Combine all components: 3ln(4/3) - 1 + Li₂(1/4)
combined_terms = three_log - 1 + li2_term

# Multiply by π/8 for final result
result = (mp.pi / 8) * combined_terms

print(mp.nstr(result, n=10))