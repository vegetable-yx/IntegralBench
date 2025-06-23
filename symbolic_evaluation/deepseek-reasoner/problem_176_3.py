import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the dilogarithm term Li_2(1/4)
dilog_term = mp.polylog(2, 1/4)

# Multiply by π/2 to get the final result
result = (mp.pi / 2) * dilog_term

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))