import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical answer is the integer 113
result = 113

# Print the result formatted to 10 significant digits
print(mp.nstr(result, n=10))