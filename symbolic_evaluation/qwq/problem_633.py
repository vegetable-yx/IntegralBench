import mpmath as mp
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Compute first term: -(pi^2)/8 * ln(2)
log2 = mp.log(2)
first_term = -(pi_sq / 8) * log2

# Compute second term: 7/16 * zeta(3)
zeta_3 = mp.zeta(3)
second_term = (7 / 16) * zeta_3

# Combine terms for final result
result = first_term + second_term

print(mp.nstr(result, n=10))