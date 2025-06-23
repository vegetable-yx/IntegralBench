import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Li_2(1/4) using the polylog function
li2_plus = mp.polylog(2, 0.25)

# Calculate Li_2(-1/4) using the polylog function
li2_minus = mp.polylog(2, -0.25)

# Compute the difference: Li_2(1/4) - Li_2(-1/4)
diff = li2_plus - li2_minus

# Multiply the difference by 1/2 to get the final result
result = 0.5 * diff

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))