import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute intermediate constants
sqrt2 = mp.sqrt(2)  # sqrt(2)
a = 1 + sqrt2       # argument for logarithm
ln_a = mp.log(a)    # ln(1 + sqrt(2))
ln2 = mp.log(2)     # ln(2)

# Argument for polylogarithms: 1 - 1/sqrt(2)
b = 1 - 1/sqrt2

# Compute polylogarithmic terms
li2_b = mp.polylog(2, b)  # Li_2(1 - 1/sqrt(2))
li3_b = mp.polylog(3, b)  # Li_3(1 - 1/sqrt(2))

# Compute individual terms in the expression
term1 = 12 * ln_a**3
term2 = -6 * ln2 * ln_a**2
term3 = -24 * ln_a * li2_b
term4 = 16 * li3_b
term5 = mp.pi**2 * ln_a

# Sum all terms and divide by 96
total = term1 + term2 + term3 + term4 + term5
result = total / 96

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))