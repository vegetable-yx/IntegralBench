import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Assign the constant value 18 to the result variable
result = 18

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))