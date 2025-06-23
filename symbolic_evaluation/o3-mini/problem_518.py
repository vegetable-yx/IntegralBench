import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the constant value 4036 to the result variable
result = mp.mpf(4036)

# Print the result to exactly 10 significant digits
print(mp.nstr(result, n=10))