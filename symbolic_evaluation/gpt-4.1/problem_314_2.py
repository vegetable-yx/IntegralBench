import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the trilogarithm Li_3(1/4)
li3_value = mp.polylog(3, mp.mpf('0.25'))

# Multiply by -1/4 to get the final result
result = -0.25 * li3_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))