import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate ln(4/3)
ln_4_over_3 = mp.log(mp.mpf(4)/3)

# Compute the term 66 * ln(4/3)
term_66_ln = 66 * ln_4_over_3

# Calculate the dilogarithm term Li_2(1/4)
li2_term = mp.polylog(2, mp.mpf(1)/4)

# Compute the term 4 * Li_2(1/4)
term_4_li2 = 4 * li2_term

# Combine all terms and subtract 19
combined = term_66_ln + term_4_li2 - 19

# Multiply by pi and divide by 128 to get the final result
result = (combined * mp.pi) / 128

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))