import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Assign the constant value 17 to the result variable
result = 17

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))