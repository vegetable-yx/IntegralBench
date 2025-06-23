import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate individual dilogarithm terms
li2_positive = mp.polylog(2, 0.25)  # Li₂(1/4)
li2_negative = mp.polylog(2, -0.25)  # Li₂(-1/4)

# Compute the difference between dilogarithm terms
dilog_difference = li2_positive - li2_negative

# Multiply by π/4 to get final result
result = (mp.pi / 4) * dilog_difference

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))