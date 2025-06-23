import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 506 * π using high-precision arithmetic
coefficient = mp.mpf(506)
result = mp.pi

# Multiply coefficient by π
final_result = coefficient * result

# Print the result with exactly 10 decimal places
print(mp.nstr(final_result, n=10))