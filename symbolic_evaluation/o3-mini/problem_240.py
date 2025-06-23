import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute ln(2) using mpmath's log function
ln2 = mp.log(2)

# Compute the constant 1/2 as a high-precision float
half = mp.mpf(1)/2

# Combine the results: ln(2) - 1/2
result = ln2 - half

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))