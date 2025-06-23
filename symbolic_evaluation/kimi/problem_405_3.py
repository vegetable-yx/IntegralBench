import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute each term in the series: 1, e, e^2, e^3
term0 = 1
term1 = mp.e
term2 = mp.e**2
term3 = mp.e**3

# Sum all the terms
series_sum = term0 + term1 + term2 + term3

# Multiply the sum by 2
result = 2 * series_sum

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))