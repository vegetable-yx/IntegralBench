import mpmath as mp

# Set internal decimal precision to 15 for accurate results
mp.dps = 15

# Compute pi squared divided by 24
term1 = mp.pi ** 2 / 24

# Compute pi multiplied by natural log of 2, then divided by 8
term2 = (mp.pi * mp.log(2)) / 8

# Compute square of natural log of 2, then divided by 4
term3 = (mp.log(2) ** 2) / 4

# Combine terms: term1 + term2 - term3
result = term1 + term2 - term3

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))