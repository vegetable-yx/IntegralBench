import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the exact analytical result: 0
result = mp.mpf(0)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))