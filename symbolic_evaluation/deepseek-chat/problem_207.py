import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the first term: (2/5) * arctan(2)
term1 = (mp.mpf(2)/5) * mp.atan(2)

# Calculate the second term: (1/10) * ln(5)
term2 = (mp.mpf(1)/10) * mp.log(5)

# Combine terms: result = term1 - term2
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))