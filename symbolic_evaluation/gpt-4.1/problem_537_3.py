import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the constant value 3 to the result variable
result = mp.mpf(3)

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))