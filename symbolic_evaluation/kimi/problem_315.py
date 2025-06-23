import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi**2

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute first term: - (pi^2 / 6) * ln(2)
term1 = -(pi_squared / 6) * ln2

# Compute second term: pi^2 / 12
term2 = pi_squared / 12

# Sum both terms to get final result
result = term1 + term2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))