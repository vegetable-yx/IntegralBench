import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the constant value 7 to the result variable
result = 7

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))