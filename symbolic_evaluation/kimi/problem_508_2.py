import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Define the constant value from the analytical expression
result = mp.mpf(4)

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))