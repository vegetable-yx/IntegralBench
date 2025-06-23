import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate pi divided by 2
result = mp.pi / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))