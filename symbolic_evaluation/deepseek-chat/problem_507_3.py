import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical answer is a constant: 18
result = mp.mpf(18)

# Print the result with 10 significant digits
print(mp.nstr(result, n=10, min_fixed=-100, max_fixed=100))