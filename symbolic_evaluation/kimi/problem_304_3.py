import mpmath as mp

mp.dps = 15  # Set decimal places for internal calculations

# Calculate the first term: -π√3/12
pi_term = mp.pi
sqrt3 = mp.sqrt(3)
term1 = -(pi_term * sqrt3) / 12

# Calculate the second term: 11/18
term2 = mp.mpf(11) / 18

# Combine terms for final result
result = term1 + term2

print(mp.nstr(result, n=10))