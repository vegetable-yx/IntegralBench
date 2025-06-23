import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate each term of the expression separately
# Term 1: (19/4) * sinh(5)
term1 = mp.fdiv(19, 4) * mp.sinh(5)

# Term 2: (31/20) * cosh(5)
term2 = mp.fdiv(31, 20) * mp.cosh(5)

# Term 3: Constant 11/5
term3 = mp.fdiv(11, 5)

# Sum all terms to get the final result
result = term1 + term2 + term3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))