import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the first term: π/4
term1 = mp.pi / 4

# Calculate the second term: (1/2) * ln(2)
term2 = 0.5 * mp.log(2)

# Third term is constant: -1
term3 = -1

# Sum all terms to get the result
result = term1 + term2 + term3

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))