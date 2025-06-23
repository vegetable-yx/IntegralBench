import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the constant value 4 to the result variable
result = mp.mpf(4)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))