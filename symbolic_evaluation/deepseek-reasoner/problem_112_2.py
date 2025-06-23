import mpmath as mp
mp.dps = 15

# Calculate fundamental constants
sqrt2 = mp.sqrt(2)
pi = mp.pi
ln2 = mp.log(2)

# Break down components of the parentheses
term1 = mp.mpf(1)
term2 = term1 / sqrt2  # 1/sqrt(2)
term3 = (mp.mpf(3)/2) * ln2  # (3/2)ln2
term4 = mp.log(1 + sqrt2)  # ln(1 + sqrt(2))

# Combine terms inside parentheses
parentheses_sum = term1 - term2 - term3 + term4

# Multiply by 4*sqrt(2)*pi
result = 4 * sqrt2 * pi * parentheses_sum

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))