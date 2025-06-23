import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute natural log of 2
ln2 = mp.log(2)

# Compute the first term: (π/8) * (ln2)^2
term1 = (mp.pi / 8) * (ln2 ** 2)

# Compute 1/sqrt(2)
inv_sqrt2 = 1 / mp.sqrt(2)

# Compute the dilogarithm for positive argument: Li₂(1/sqrt(2))
dilog_plus = mp.polylog(2, inv_sqrt2)

# Compute the dilogarithm for negative argument: Li₂(-1/sqrt(2))
dilog_minus = mp.polylog(2, -inv_sqrt2)

# Compute the second term: (1/2) * [Li₂(1/sqrt(2)) - Li₂(-1/sqrt(2))]
term2 = 0.5 * (dilog_plus - dilog_minus)

# Sum both terms to get the final result
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))