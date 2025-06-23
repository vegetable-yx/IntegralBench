import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the dilogarithm values for 1/4 and -1/4
li2_1_over_4 = mp.polylog(2, 1/4)
li2_minus_1_over_4 = mp.polylog(2, -1/4)

# Calculate the difference between the two dilogarithm values
difference = li2_1_over_4 - li2_minus_1_over_4

# Multiply by 1/2 to get the final result
result = 0.5 * difference

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))