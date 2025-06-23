import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Define the analytical expression: -1/16
result = mp.mpf('-1') / mp.mpf('16')

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))