import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the first hypergeometric term: (1/2) * _1F_2(1; 3/2, 2; -1)
term1 = 0.5 * mp.hyper([1], [mp.mpf('3/2'), 2], -1)

# Calculate the second hypergeometric term: (1/3) * _1F_2(1; 2, 5/2; -1)
term2 = mp.mpf('1/3') * mp.hyper([1], [2, mp.mpf('5/2')], -1)

# Combine the terms to get the final result
result = term1 - term2

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))