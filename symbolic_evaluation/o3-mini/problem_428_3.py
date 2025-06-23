import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical answer is the constant 17
result = mp.mpf(17)

# Print the result to exactly 10 significant digits
print(mp.nstr(result, n=10))