import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# The analytical expression is a constant: 2
result = mp.mpf(2)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))