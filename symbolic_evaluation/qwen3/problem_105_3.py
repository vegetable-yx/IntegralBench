import mpmath as mp
mp.dps = 15

# Calculate each term of the expression separately
pi_squared = mp.pi ** 2
term1 = pi_squared / 18  # π²/18 component

sqrt3 = mp.sqrt(3)
term2 = (mp.pi * sqrt3) / 9  # (π√3)/9 component

term3 = mp.mpf(2)/3  # 2/3 constant term

# Combine all terms to get the final result
result = term1 + term2 - term3

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))