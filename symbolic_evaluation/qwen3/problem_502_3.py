import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the first term: 10747 divided by 10
term1 = mp.mpf(10747)/10

# Calculate the logarithmic term: 6 * natural log of 2
term2 = 6 * mp.log(2)

# Combine both terms for final result
result = term1 + term2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))