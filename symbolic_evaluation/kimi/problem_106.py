import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the dilogarithm terms
dilog_half = mp.polylog(2, 0.5)
dilog_minus_half = mp.polylog(2, -0.5)

# Combine terms according to the analytical solution
result = 2 * (dilog_half - dilog_minus_half)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))