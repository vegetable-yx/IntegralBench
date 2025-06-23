import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Euler's number e is a fundamental mathematical constant
result = mp.e

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))