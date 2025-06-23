import mpmath as mp
mp.dps = 15

# Calculate the first term: 10747 divided by 10
term1 = mp.mpf(10747) / 10

# Calculate the second term: 6 multiplied by natural logarithm of 2
term2 = 6 * mp.log(2)

# Sum both terms to get final result
result = term1 + term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))