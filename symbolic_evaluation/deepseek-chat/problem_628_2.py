import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate each term of the expression: -1/4 + π/8
term1 = mp.mpf('-0.25')  # Exactly -1/4
term2 = mp.pi / 8        # π divided by 8

# Sum the terms to get the result
result = term1 + term2

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))