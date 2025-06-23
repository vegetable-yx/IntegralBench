import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the first term: 10747 divided by 10
term1 = mp.mpf(10747)/10

# Calculate the second term: 6 times natural logarithm of 2
term2 = 6 * mp.log(2)

# Sum both terms to get final result
result = term1 + term2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))