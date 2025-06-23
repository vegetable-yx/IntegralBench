import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate π for reuse
pi_val = mp.pi

# Compute each term of the expression separately

# Term 1: (π^3 / 216) * ln(2)
pi_cubed = pi_val ** 3
log2_val = mp.log(2)
term1 = (pi_cubed / 216) * log2_val

# Term 2: (π / 12) * Li_3(1/2)
li3_half = mp.polylog(3, 0.5)
term2 = (pi_val / 12) * li3_half

# Term 3: (π / 24) * ζ(3) [this term is subtracted]
zeta3_val = mp.zeta(3)
term3 = (pi_val / 24) * zeta3_val

# Combine terms: term1 + term2 - term3
result = term1 + term2 - term3

# Print the final result rounded to 10 decimal places
print(mp.nstr(result, n=10))