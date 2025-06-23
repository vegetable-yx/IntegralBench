import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# The analytical expression is the constant π
result = mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))