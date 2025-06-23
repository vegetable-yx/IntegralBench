import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the constant term
term1 = mp.mpf(-1)

# Calculate pi/4
term2 = mp.pi / 4

# Calculate (1/2) * ln(2)
term3 = mp.mpf(0.5) * mp.log(2)

# Sum all terms
result = term1 + term2 + term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))