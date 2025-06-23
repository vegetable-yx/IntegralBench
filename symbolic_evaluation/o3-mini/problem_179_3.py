import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the first hypergeometric term: _1F_2(1; 3/2, 3; -1)
term1 = mp.hyp1f2(1, mp.mpf(3)/2, 3, -1)

# Calculate the second hypergeometric term: _1F_2(1; 2, 7/2; -1)
term2 = mp.hyp1f2(1, 2, mp.mpf(7)/2, -1)

# Combine terms according to the expression: (32*term1 - term2)/128
result = (32 * term1 - term2) / 128

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))