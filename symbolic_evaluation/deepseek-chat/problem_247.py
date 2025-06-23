import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the value of 1/32
result = mp.mpf(1) / mp.mpf(32)

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))