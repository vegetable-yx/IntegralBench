import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is the constant 4
result = mp.mpf('4.000000000')  # Represent 4 with 10 significant digits (4 followed by 9 zeros)

# Output the result to exactly 10 significant digits
print(mp.nstr(result, n=10))