import mpmath as mp

# Set internal decimal precision to 15 digits for reliable calculations
mp.dps = 15

# The analytical expression is the constant integer 17
result = mp.mpf(17)

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))