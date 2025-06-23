import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Define constants and repeated subexpressions
sqrt2 = mp.sqrt(2)  # √2
one_plus_sqrt2 = 1 + sqrt2  # 1 + √2

# Compute ln(1 + √2)
ln_term = mp.log(one_plus_sqrt2)

# Compute 1/(1+√2)
reciprocal = 1 / one_plus_sqrt2

# Compute the polylogarithm difference: Li_3(1/(1+√2)) - Li_3(-1/(1+√2))
li3_diff = mp.polylog(3, reciprocal) - mp.polylog(3, -reciprocal)

# Calculate each term of the expression
# Term 1: 3 * π^3 * (16 - 11√2)
term1 = 3 * mp.pi**3 * (16 - 11 * sqrt2)

# Term 2: 32 * (√2 - 16) * π * [ln(1+√2)]^2
term2 = 32 * (sqrt2 - 16) * mp.pi * ln_term**2

# Term 3: 256 * √2 * [ln(1+√2)]^3
term3 = 256 * sqrt2 * ln_term**3

# Term 4: 768 * (√2 - 1) * (Li_3(reciprocal) - Li_3(-reciprocal))
term4 = 768 * (sqrt2 - 1) * li3_diff

# Sum all terms and divide by 3072
result = (term1 + term2 + term3 + term4) / 3072

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))