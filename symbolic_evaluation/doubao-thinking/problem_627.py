import mpmath as mp

# Set internal decimal precision to 15 to ensure 10 decimal places accuracy
mp.dps = 15

# Calculate pi/4
term1 = mp.pi / 4

# Calculate natural logarithm of 2
ln2 = mp.log(2)
# Then (ln2)/2
term2 = ln2 / 2

# Constant term: -1
term3 = -1

# Sum all terms: pi/4 + (ln2)/2 - 1
result = term1 + term2 + term3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))