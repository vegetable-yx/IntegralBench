import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Define frequently used constants and expressions
pi = mp.pi
sqrt2 = mp.sqrt(2)
log_1_plus_sqrt2 = mp.log(1 + sqrt2)
log2 = mp.log(2)

# Break down the expression into manageable terms
term1 = pi / 2
term2 = - (pi * sqrt2) / 4
term3 = (sqrt2 / 2) * log_1_plus_sqrt2
term4 = - (pi / 2) * log_1_plus_sqrt2
term5 = (pi / 4) * log2

# Sum all terms to get the final result
result = term1 + term2 + term3 + term4 + term5

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))