import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Analytical expression is 0
result = mp.mpf(0)

# Print the result to exactly 10 decimal places using mp.nstr formatting
print(mp.nstr(result, n=10))