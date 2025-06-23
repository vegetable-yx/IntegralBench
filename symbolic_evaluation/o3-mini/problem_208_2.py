import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute ln(2)
ln2 = mp.log(2)

# Compute ln^2(2)
ln2_sq = ln2**2

# Compute π^2
pi_sq = mp.pi**2

# Compute dilogarithm terms: Li_2(1/2) and Li_2(-1/2)
Li2_half = mp.polylog(2, 0.5)
Li2_neg_half = mp.polylog(2, -0.5)

# Compute numerator: π^2 + 8*ln^2(2) - 16*Li_2(1/2) + 16*Li_2(-1/2)
numerator = pi_sq + 8*ln2_sq - 16*Li2_half + 16*Li2_neg_half

# Divide numerator by 96
term1 = numerator / 96

# Compute constant term 7/18
term2 = mp.mpf(7)/18

# Sum both terms for final result
result = term1 + term2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))