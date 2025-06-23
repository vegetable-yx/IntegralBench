import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate term1: ln(2)/4
term1 = mp.log(2) / 4

# Calculate the expression inside the logarithm for term2: 3 + 2*sqrt(2)
inner_log = 3 + 2 * mp.sqrt(2)

# Calculate term2: (sqrt(2)/2) * ln(3 + 2*sqrt(2))
term2 = (mp.sqrt(2) / 2) * mp.log(inner_log)

# Calculate the constant term: -2
term3 = -2

# Sum all terms to get the final result
result = term1 + term2 + term3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))