import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Define frequently used constants and expressions
sqrt2 = mp.sqrt(2)
a = 1 + sqrt2  # 1 + sqrt(2)
b = (sqrt2 - 1)**2  # (sqrt(2) - 1)^2
c = 1 - 1/sqrt2  # 1 - 1/sqrt(2)
d = 1 - sqrt2  # 1 - sqrt(2)

# Compute logarithmic terms
ln_a = mp.log(a)

# Compute polylogarithmic terms
li2_b = mp.polylog(2, b)
li3_b = mp.polylog(3, b)
li3_c = mp.polylog(3, c)
li3_d = mp.polylog(3, d)

# Calculate each term of the expression
term1 = (mp.pi / 16) * ln_a**3
term2 = (-3/16) * ln_a * li2_b
term3 = (1/16) * li3_b
term4 = (1/8) * (li3_c - li3_d)

# Sum all terms to get the final result
result = term1 + term2 + term3 + term4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))