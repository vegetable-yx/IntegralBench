import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute the polylogarithm of order 3 at -1/2
term1 = mp.polylog(3, -0.5)

# Compute the polylogarithm of order 3 at 1/2
term2 = mp.polylog(3, 0.5)

# Calculate the difference: Li_3(-1/2) - Li_3(1/2)
result = term1 - term2

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))