import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Li_2(1/4)
li2_1_4 = mp.polylog(2, 1/4)

# Compute Li_2(-1/4)
li2_neg_1_4 = mp.polylog(2, -1/4)

# Calculate the difference between the two dilogarithm values
numerator = li2_1_4 - li2_neg_1_4

# Divide by 2 to get the final result
result = numerator / 2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))