import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute the rational term: 10747 divided by 10
rational_term = mp.mpf(10747) / mp.mpf(10)

# Compute the logarithmic term: 6 multiplied by natural logarithm of 2
log_term = 6 * mp.log(2)

# Sum the two terms to get the final result
result = rational_term + log_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))