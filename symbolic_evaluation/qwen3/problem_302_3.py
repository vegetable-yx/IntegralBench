import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Li_2(1/4)
li2_1_4 = mp.polylog(2, 1/mp.mpf(4))

# Calculate Li_2(-1/4)
li2_minus1_4 = mp.polylog(2, -1/mp.mpf(4))

# Compute the difference between the two dilogarithm values
difference = li2_1_4 - li2_minus1_4

# Divide the difference by 2 to get the final result
result = difference / 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))