import mpmath as mp

# Set internal precision to 15 decimal places for intermediate calculations
mp.dps = 15

# The analytical expression is the constant 0
result = mp.mpf(0)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))