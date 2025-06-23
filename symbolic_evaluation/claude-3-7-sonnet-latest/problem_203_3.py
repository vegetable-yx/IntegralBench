import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the exact value of the expression: 8 divided by 3
result = mp.mpf(8) / mp.mpf(3)

# Print the result rounded to exactly 10 decimal places
print(mp.nstr(result, n=10))