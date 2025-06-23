import mpmath as mp

# Set the internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Assign the constant π to the result variable
result = mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))