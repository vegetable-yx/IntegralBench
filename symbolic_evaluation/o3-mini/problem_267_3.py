import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Define constants and values
ln2 = mp.log(2)
pi_val = mp.pi

# Compute Li2(1/4) - dilogarithm
li2_1_4 = mp.polylog(2, 0.25)

# Compute Li3(1/4) - trilogarithm
li3_1_4 = mp.polylog(3, 0.25)

# Compute Li3(-1/2) - trilogarithm
li3_neg_half = mp.polylog(3, -0.5)

# Calculate each term of the expression
term1 = (pi_val * ln2**2) / 16
term2 = (ln2 * li2_1_4) / 8
term3 = -li3_1_4 / 16
term4 = -li3_neg_half / 16

# Sum all terms for final result
result = term1 + term2 + term3 + term4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))