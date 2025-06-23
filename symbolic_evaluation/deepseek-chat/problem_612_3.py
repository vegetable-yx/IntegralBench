import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the constant value 626 to result
result = mp.mpf(626)

# Print the result to exactly 10 decimal places using mpmath's nstr
print(mp.nstr(result, n=10))