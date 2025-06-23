import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate pi squared divided by 8
term1 = mp.pi**2 / 8

# Calculate natural log of 2
ln2 = mp.log(2)

# Calculate (ln2)^2
ln2_sq = ln2**2

# Calculate (pi * (ln2)^2) / 4
term2 = (mp.pi * ln2_sq) / 4

# Calculate dilogarithm of 1/2
dilog_half = mp.polylog(2, 0.5)

# Multiply dilog(1/2) by 1/2
term3 = 0.5 * dilog_half

# Combine the terms: term1 - term2 - term3
result = term1 - term2 - term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))