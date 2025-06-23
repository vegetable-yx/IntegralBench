import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate (ln 2)^2
ln2 = mp.log(2)
ln2_squared = ln2 ** 2

# Calculate first term: (ln2)^2 / 4
term1 = ln2_squared / 4

# Calculate pi squared
pi_squared = mp.pi ** 2

# Calculate second term: pi^2 / 48
term2 = pi_squared / 48

# Sum the terms to get final result
result = term1 + term2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))