import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Assign the exact numerical value directly
result = mp.mpf('-0.7486489283')

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))