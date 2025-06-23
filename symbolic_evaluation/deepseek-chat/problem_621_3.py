import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Assign the constant value -1 to the result variable
result = mp.mpf(-1)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))