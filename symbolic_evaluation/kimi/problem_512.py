import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate the square of Euler's number (e^2)
e_squared = mp.e ** 2

# Compute the first term: e^2 divided by 4
term1 = e_squared / 4

# Compute the second term: 1/4
term2 = mp.mpf(1) / 4

# Combine terms: term1 minus term2
result = term1 - term2

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))