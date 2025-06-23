import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 506 * π using high-precision arithmetic
pi_value = mp.pi
result = 506 * pi_value

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))