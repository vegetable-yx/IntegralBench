import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate common constant: 1 + sqrt(2)
a = 1 + mp.sqrt(2)

# Compute ln(1 + sqrt(2))
ln_a = mp.log(a)

# Compute ln^3(1 + sqrt(2))
ln_a_cubed = ln_a ** 3

# First term: (pi/8) * ln^3(1 + sqrt(2))
term1 = (mp.pi / 8) * ln_a_cubed

# Compute argument for polylogarithms: 2*sqrt(2) - 2
b = 2 * mp.sqrt(2) - 2

# Compute dilogarithm Li_2(2*sqrt(2)-2)
Li2_b = mp.polylog(2, b)

# Second term: [ln(1+sqrt(2))/4] * Li_2(2*sqrt(2)-2)
term2 = (ln_a / 4) * Li2_b

# Compute trilogarithm Li_3(2*sqrt(2)-2)
Li3_b = mp.polylog(3, b)

# Third term: -1/8 * Li_3(2*sqrt(2)-2)
term3 = (-1/8) * Li3_b

# Sum all terms
result = term1 + term2 + term3

# Print result to 10 decimal places
print(mp.nstr(result, n=10))