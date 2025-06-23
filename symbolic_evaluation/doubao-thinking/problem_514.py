import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate the first term: pi divided by 6
term1 = mp.pi / 6

# Calculate the second term: square root of 3 divided by 8
term2 = mp.sqrt(3) / 8

# Sum the two terms to get the final result
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))