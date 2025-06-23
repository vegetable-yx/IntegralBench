import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Compute the constant term: -1/2
term1 = mp.mpf('-0.5')

# Compute the logarithmic term: - (1/4) * ln(2)
ln2 = mp.log(2)  # Natural logarithm of 2
term2 = mp.mpf('-0.25') * ln2

# Compute the pi-squared term: π² / 24
pi_squared = mp.pi ** 2
term3 = pi_squared / mp.mpf('24')

# Sum all terms to get the final result
result = term1 + term2 + term3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))